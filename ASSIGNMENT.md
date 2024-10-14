# OOP Assignment Example

## Specification

In this assignment, you are asked to develop an object-oriented library to play the game of [Azul](https://boardgamegeek.com/boardgame/230802/azul) (a PDF version of the rules has been provided). It is not expected that you provide a full, working implementation of the game: rather, the intent is to expose you to numerous opportunities to showcase your object-oriented design and implementation skills on a concrete, relatable example.

Your library should expose a class `Game` to its users, which can be instantiated to create a new game (with given initial parameters, if relevant). The public instance properties and methods of `Game` should allow the game to be played according to the rules and expose all necessary game information. More precisely, the `Game` class must provide the API to your library:

1. **It must be possible to play the game and access game information in a programmatic way. This should follow an object-oriented design, delegating responsibilities to suitable sub-components whose public methods and properties allow the game to be played.** As a rule of thumb, imagine whether a suitably well-crafted algorithm would be able to fully play the game through your public `Game` interface. Common issues:
   - Printing information to console and/or requiring user input from console (or other UI).
   - Exposing gameplay methods, but not giving access to the full game information.
   - Inadequately delegating responsibility for action execution and/or information exposure to sub-components.

2. **Code executing illegal actions must not statically type-check, or it must otherwise raise an error at runtime. This includes playing illegal moves and other illegal modification of the game state/information (i.e. if encapsulation is broken).** In other words, the public methods and properties of the `Game` class and any sub-components which it exposes must not allow illegal actions to be performed. Common issues:
   - Methods can be successfully invoked with illegal parameters, or in illegal order.
   - Mutable public properties allow illegal values to be set.
   - Read-only properties expose objects which can themselves be illegally modified.

Note that it must be possible to create multiple independent instances of `Game` at the same time (e.g. to use the library as part of an online game server). The user interface (console-based or otherwise) is out of scope for this assignment and will not contribute to its mark: if you wish to provide one, e.g. to explain the intended usage of your code, it should be built entirely on top of the `Game` API.

Please note that you will be **heavily penalised** if it is not possible to play the game programmatically, as this prevents me from adequately judging other assessment criteria.

## Task

Design and implement a library with the functionality described above, using an object oriented approach:

- Low-level data used by the library should be structured by means of suitable types (try to avoid classes for lightweight data) and validated where necessary. As much data validation as reasonably possible should be delegated to the static type-checking.
- High-level components used by the library should be structured through classes, with public methods providing access to external functionality and protected/private methods providing access to internal functionality. Functionality should be delegated to sub-components, in a balanced way: implementing most logic in the `Game` class is unlikely to earn you high marks.
- Your design should make use of adequately chosen types, read-only properties, protected/private attributes and other forms of access control to ensure that the library cannot be misused. This should be balanced with the need for individual components to safely expose their information to your library's users. Access control so tight as to prevent the exposure of information is unlikely to earn you high marks.
- Where relevant, you should attempt to use advanced type features (e.g. inheritance, composition, generics, method overloads, structural types).
- Where relevant, you should attempt to use advanced language features (e.g. comprehensions, iterators, dunder methods, function objects).
- Where relevant, you should attempt to use object-oriented patterns. You are advised not to use the singleton pattern unless you find a compelling reason to do so (in which case, you should carefully explain it).
- Where relevant, you should attempt to implement reusable generic data structures.

Your code should be clear and concise: long or complex method/function bodies should be avoided whenever possible (e.g. by delegating to helper methods/functions, or to sub-components). Where long or complex code is unavoidable, the individual steps should be concisely documented using single-line comments.

## Submission

You should clearly document your code to explain its design and implementation: all classes, methods, functions and globals should be documented using Python docstrings.
I'm happy with plaintext documentation, but if you want to learn something useful in real-life Python projects you might consider writing [Sphinx](https://www.sphinx-doc.org)-compatible documentation in [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#rst-primer).

Please include a `README.md` with the following information:

- Which advanced type features (if any) have been used.
- Which object oriented patterns (if any) have been implemented and where, with brief justification.
- Which reusable data structures (if any) have been implemented and where, with brief justification.

You might also wish to include one or more code snippets explaining how your library is intended to be used programmatically: you can do so in one or more separate scripts (not to be placed inside the `azul` package), or you can do so within the docstrings of modules, classes and methods (e.g. using Sphinx [code blocks](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-code-block)).
You should submit a single ZIP file containing the `README.md` file and the `azul` package at the top level, as well as any additional scripts.

Your implementation should be in a single Python package `azul` containing your implementation. Following the Single Responsibility Principle, your code should be adequately organised in sub-modules: imports between your sub-modules should be relative &mdash; using `.module_name` if the import is from the same level or `..module_name` if the import is from parent level &mdash; and your main package should contain a `__init__.py` file exporting only the `Game` class:

```py
"""
Documentation for the main game package.
"""

from .game import Game

__all__ = ("Game", )
```

If you use folders for better organisation of code in your sub-modules, please remember to add a `__init__.py` file to each folder to turn it into a package.

Please use Python 3.12 with:

- `mypy --strict azul` for static type-checking (use ``python -m pip install mypy==1.11.2``).
- `black -l 80 azul` for automatic formatting (any recent version).

Static type-checking errors will be **heavily penalised**. If your design is particularly sophisticated, you might find yourself in need of the `type: ignore` directive or the `Any` type: if this happens, please include a comment with detailed justification on each occurrence, or I will consider them to be equivalent to errors.

Please enable [PEP 563 – Postponed Evaluation of Annotations](https://peps.python.org/pep-0563/) by placing the following line at the top of your module imports:

```py
from __future__ import annotations
```

PEP 563 will be ultimately superseded by [PEP 649 – Deferred Evaluation Of Annotations Using Descriptors](https://peps.python.org/pep-0649/) in Python 3.14, but for now it fixes some important issues with Python's static type annotations.

## Assessment Criteria

Assessment will be based on the following criteria:

- Can you use an object-oriented approach to design libraries, algorithms and data structures?
- Can you implement libraries, algorithms and data structures using object-oriented languages in a structured, type-safe, re-usable way?
- Can you explain the rationale behind your object-oriented design and implementation?
- Can you write clear, maintainable code, making use of idiomatic language features and following language conventions?
