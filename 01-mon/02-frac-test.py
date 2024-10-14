"""
Script to test the module :mod:`frac`.
"""

from decimal import Decimal
from fractions import Fraction
from typing import Any
# There are good builtin Fraction and Decimal classes.
# This is only for educational purposes!

# print("In 02-frac-test.py, just before import frac_v1")

import frac_v1 # imports the module as an object

# print("In 02-frac-test.py, just after import frac_v1")

print(f"{frac_v1 = }")
# <module 'frac_v1' from '...\\oop-course-oct-2024\\01-mon\\frac_v1.py'>

print(f"{frac_v1.PI = }")                 # frac_v1.PI = Frac(22, 7)
print(f"frac_v1.PI = {repr(frac_v1.PI)}") # frac_v1.PI = Frac(22, 7)
#                     ^^^^ builtin function calling __repr__ under the hood
print(f"frac_v1.PI = {frac_v1.PI!r}") # frac_v1.PI = Frac(22, 7)
#                               ^^ equivalent to calling repr(...)
print(f"A simple approx of PI is {frac_v1.PI}")
# A simple approx of PI is Frac(22, 7)

from frac_v1 import Frac as FracV1
# A named import, with an alias
# This is because I will want to import multiple versions of a Frac class,
# and I want to avoid conflicts.

print(FracV1(20, 10) == FracV1(10, 5))
#                    ^^ binary operator implemented by __eq__

# Tests to explain how NotImplemented works.

class A:
    _x: int
    def __init__(self, x: int) -> None:
        self._x = x
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, A):
            # The designers of class A didn't care about the wishes
            # of other designers who might want their classes to play
            # well with class A.
            return False
        return self._x == other._x

class B:
    _s: str
    def __init__(self, s: str) -> None:
        self._s = s

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, A):
            return len(self._s) == other._x
        if not isinstance(other, B):
            # The designers of class B are hypocrites who want to play
            # with class A, but don't care about others playing with class B.
            return False
        return self._s == other._s

print(f"{A(5) == B("hello") = }") # False
# same as A(5).__eq__(B("hello")) uses the __eq__ of class A
print(f"{B("hello") == A(5) = }") # True
# same as B("hello").__eq__(A(5)) uses the __eq__ of class B


class A1:
    _x: int
    def __init__(self, x: int) -> None:
        self._x = x
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, A1):
            # The designers of class A didn't care about the wishes
            # of other designers who might want their classes to play
            # well with class A.
            return NotImplemented
        return self._x == other._x

class B1:
    _s: str
    def __init__(self, s: str) -> None:
        self._s = s

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, A1):
            return len(self._s) == other._x
        if not isinstance(other, B1):
            # The designers of class B are hypocrites who want to play
            # with class A, but don't care about others playing with class B.
            return NotImplemented
        return self._s == other._s

print(f"{A1(5) == 10 = }")      # False (NotImplemented doesn't show up)
# same as A1(5).__eq__(10), uses the __eq__ of class A1
# returns NotImplemented, which tells the runtime to look at __eq__ of class int
# which returns NotImplemented, and that translates to False in the end.
print(f"{A1(5) == B1("hello") = }") # True
# same as A1(5).__eq__(B1("hello")), uses the __eq__ of class A1
# returns NotImplemented, which tells the runtime to look at __eq__ of class B1
# which returns True, and that's the final result.
print(f"{B1("hello") == A1(5) = }") # True

my_frac = FracV1(20, 5)
print(f"{my_frac.num = }") # my_frac.num = 20
# my_frac.num = 22 # Error: Property "num" defined in "Frac" is read-only
print(f"{my_frac.den = }") # my_frac.num = 5
print(f"{my_frac.float = }") # my_frac.float = 4.0
#                ^^^^^ behaves like a stored attribute
#                      but it is computed on the fly.

print(f"{FracV1(1, 3).add(FracV1(22, 7)).neg()}") # -73/21

from frac_v2 import Frac as FracV2

my_frac2 = FracV2(22, 7)
print(f"{my_frac2.den = }") # OK, my_frac2.den = 7
# print(f"{my_frac2.__den = }")
# Would raise AttributeError: 'Frac' object has no attribute '__den'
# The private name __den is name-mangled to _Frac__den:
print(f"{my_frac2.__dict__ = }") # {'_Frac__num': 22, '_Frac__den': 7}
#                 ^^^^^^^^ special attribute __dict__
# system dictionary containing the values of attributes of an object
# (Terms and conditions apply see __slots__ later on.)
# {'_Frac__num': 22, '_Frac__den': 7}
#        ^^^^^ name from inside Frac
#   ^^^^^^^^^^ name from outside Frac
print(f"{my_frac2._Frac__num = }") # type: ignore # my_frac2._Frac__num = 22
# silencing mypy 'cause it's stupid^^^^^^^^^^^^^^

print(f"{-(FracV2(1, 3)+(FracV2(22, 7)))}") # -73/21

x = FracV2(2, 3)
pi = FracV2(22, 7)
z = FracV2(-3, 5)

print(f"{x*pi/z = !s}") # x*pi/z = -220/63
#                 ^^ use str instead of repr

print(f"{(x*pi/z)+2 = !s}") # (x*pi/z)+2 = -94/63
#                ^ Frac.__add__(int)
print(f"{2+(x*pi/z) = !s}") # 2+(x*pi/z) = -94/63
#         ^ int.__add__(Frac), and int.__add__ does not support Frac

print(f"{2/(x*pi/z) = !s}") # 2/(x*pi/z) = -63/110

print(f"{FracV2.PI = !s}") # FracV2.PI = 22/7

class MyRandoClass:
    ...
    # This is hashable by default.

my_rando_set = {MyRandoClass(), MyRandoClass()}
print(f"{my_rando_set = }")
# my_rando_set = {
#     <__main__.MyRandoClass object at 0x00000257996F1CA0>,
#     <__main__.MyRandoClass object at 0x00000257996F1CD0>
# }

my_frac_set2 = {FracV2.PI, x, z}
print(f"{my_frac_set2 = }")
# my_frac_set2 = {
#   Frac(22, 7),
#   Frac(-3, 5),
#   Frac(2, 3)
# }
