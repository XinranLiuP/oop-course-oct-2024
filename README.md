# OOP Course - Oct 2024 Materials

Materials for the Oct 2024 iteration of OOP.

## Some Python books

- [The Big Book of Small Python Projects](https://nostarch.com/big-book-small-python-projects)
- [Impractical Python Projects](https://nostarch.com/impracticalpythonprojects)
- [Dead Simple Python](https://nostarch.com/dead-simple-python)
- [Object-Oriented Python](https://nostarch.com/object-oriented-python)

## Useful references

- [Official Python Documentation](https://docs.python.org/3/)
- [Time complexity for collection operations](https://wiki.python.org/moin/TimeComplexity)
- [The ``typing`` module](https://docs.python.org/3/library/typing.html)
- [The ``collections.abc`` module](https://docs.python.org/3/library/collections.abc.html)
- [Python's Data Model](https://docs.python.org/3/reference/datamodel.html)
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)

## Visual Studio Code

You should install [VS Code](https://code.visualstudio.com/) and set it up for [Python](https://code.visualstudio.com/Docs/languages/python).
You should install the following extensions:

- the [`Python` extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- the [`Python Debugger` extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)
- the [`Mypy Type Checker` extension](https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker)

A `mypy.ini` file at the root of this repository instructs Mypy to run in strict mode.

## Command Line Tools

The [Mypy](https://github.com/python/mypy) static type-checker (in strict mode):

```py
mypy --strict <module>
```

The [Black](https://github.com/psf/black) code formatter (e.g. line length set to 80):

```py
black -l 80 <module>
```

The [Ruff](https://github.com/astral-sh/ruff) linter:

```py
ruff check <module>
```

```py
ruff format <module>
```

## Naming your local files

To avoid conflicts with the files pushed into this repository, make sure that your local working copies of files have names ending in `-local.py`, or that they are contained in folder with names ending in `-local`.
There are `.gitignore` rules set up to ignore such files and folders in commits.
