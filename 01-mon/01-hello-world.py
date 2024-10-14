"""
This is a script¹ where I will introduce some of the basic features of Python.
For example, this is a module docstring.

¹ Technically, this is a module, as every Python file is.
  In this course, I will use "script" to refer to modules which are meant to be
  executed directly and not imported. In this case, the module could not be
  imported anyway, because its name is not a valid Python identifier.
"""

from typing import Any

print("Hello World")
# This is an inline comment.

# Immutable basic types

n: None = None # conventionally used as "undefined", or "not set" in an optional
b: bool = True
x: int = 10
s: str = "Hello World" # UTF-8 strings, sequences of Unicode codepoints
s = "😼🍎"
print(s)
bs: bytes = b"Hello World\x00"
bs = bytes([0, 43, 58, 127])
print(bs) # b'\x00+:\x7f'

# Mutable collections

# List = ordered collection with repetition
int_fruit_list: list[int|str] = [0, 1, 1, "🍎", "🍋"]
#                      ^^^^^^^^^ generic type parameter
assert int_fruit_list != [0, 1, "🍎", "🍋"] # repetition matters
assert int_fruit_list != [1, 0, 1, "🍎", "🍋"] # order matters
# assert statement: raises AssertionError if condition is False at runtime
# removed in optimised execution (-O or -OO commandline flags)
# standard way to perform debug/development checks
# not a good way to perform runtime validation (unless low-level library)

# Set = unordered collection without repetition
fruit_set: set[str] = {"apple", "orange"}
assert fruit_set == {"apple", "orange", "apple"} # repetition is irrelevant
assert fruit_set == {"orange", "apple"} # order is irrelevant

# Dictionary = key-value store
fruit_count_dict: dict[str, int] = {
    "apple": 2,
    "orange": 3,
    "pear": 1
}

# Note:
# set = {item, item, item, ...}
# dict = {key: value, key: value, key: value, ...}

another_fruit_count_dict = {
    "apple": 1,
    "orange": 2,
    "pear": 2
}
# Mypy infers type dict[str, int]

empty_set: set[Any] = set() # a set
empty_dict: dict[str, Any] = {} # a dict with str keys

# Immutable collection

def process_bad_pair(pair: list[int | str]) -> None:
    """
    This function presumes that the argument passed to it
    is a pair of an int and a str.
         ^^^^       ^^^       ^^^
    """
    # Validation (3 runtime checks)
    fst, snd = pair # destructure raises ValueError if not pair
    if not isinstance(fst, int):
        raise TypeError(
            f"First argument must be integer, found {fst = }"
            # strings starting with f are f-strings
            # analogous to template strings in JavaScript and other languages
            # there's a lot of interesting printing options (we'll see)
        )
    # If code gets here, Mypy knows that fst is an int,
    # so no error on the print(fst-2).
    if not isinstance(snd, str):
        raise TypeError(
            f"Second argument must be string, found {snd = }"
        )
    # If code gets here, Mypy knows that snd is a str,
    # so no error on the print(snd.count("a")).
    print(fst-2)
    print(snd.count("a"))

some_bad_pair: list[int | str] = [1, "apple"]
process_bad_pair([1, "apples"])

# Fixed-length tuple = immutable sequence with given types for items

def process_pair(pair: tuple[int, str]) -> None:
    #                  ^^^^^^^^^^^^^^^
    # Mypy knows statically that:
    # - it is a pair
    # - the fst argument is an int
    # - the snd argument is a str
    fst, snd = pair
    print(fst-2)
    print(snd.count("a"))

# Var-length tuple = immutable homogeneous sequence of variable length

my_immutable_seq: tuple[int|str, ...] = (1, 2, "apple", "orange")
#             item type ^^^^^^^  ^^^ indicates variable length tuple
# This is akin to list[int|str], but immutable

pair_of_lists: tuple[list[int], list[str]] = ([], [])
# I cannot reassign the lists (tuple is immutable),
# but I can modify the lists themselves:
print(pair_of_lists) # ([], )
pair_of_lists[0].append(0)
pair_of_lists[1].extend(["apple", "orange"])
print(pair_of_lists) # ([0], ['apple', 'orange'])

# pair_of_lists[0] = 2
# unsupported target for indexed assignment ("tuple[list[int], list[str]]")
# tuples don't have a __setitem__ method

# Frozen set = like set, but immutable

immutable_fruit_set = frozenset({"apple", "orange"})
# frozenset[str] is like set[str], but cannot add/remove elements

