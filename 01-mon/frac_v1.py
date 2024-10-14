"""
A module with a custom implementation of fractions.

A module is any .py file whose name is a valid Python identifier,
ie any name which can be used as a legit variable name in Python code.
"""

from __future__ import annotations

from math import gcd
from typing import Any, Final

print(f"  In frac_v1.py, just before Frac, {dir() = }")
#      a list of all names defined in scope ^^^^^

assert "Frac" not in dir() # True: Frac has not been defined yet


class Frac:
    """
    A class for immutable fractions.

    A class is a way to collect data + logic pertaining to the data
    in the same place, so that common operations on the data are readily
    available wherever the data is used.
    """

    # print("    Just before declaring attributes of Frac")

    # 1. Attributes
    # Claces where data is stored (keys in a dictionary)
    # These are static type declarations, they have no runtime effect.

    _num: Final[int]
    #     ^^^^^ tells the static typechecker that this attribute
    #           should be assigned in the constructor and never again
    """
    Protected attribute for the numerator of the fraction.

    Leaving the attribute protected makes it directly accessible to subclasses.
    Because our logic presumes that the fraction is immutable,
    we mark the attribute type as Final so that subclasses cannot reassing it.

    Had we made it private, we could have done without the Final, since we are
    the only ones meant access the attribute.
    """

    _den: Final[int]
    """ Protected attribute for the denominator of the fraction. """

    # 2. Constructor
    # Creates instances of the class from given data

    def __init__(self, num: int, den: int) -> None:
        #        ^^^^ already an instance of Frac, created somewhere else.
        """
        Initialiser (not technically a constructor).

        Validates constructor data and sets values for the attributes.
        Not responsible for the instance creation process.
        """
        # 1. Validation
        if den == 0:
            raise ZeroDivisionError()
        if den < 0:
            num, den = -num, -den
        # 2. Setting attributes
        self._num = num
        self._den = den

    # 3. Properties
    # Provide readonly (by default) access to class data
    # Can be used to give safe access to protected attributes,
    # but also to synthesise new data based on attributes.

    @property
    def num(self) -> int:
        """ Provides read-only access to the contents of _num. """
        return self._num
    @property
    def den(self) -> int:
        """ Provides read-only access to the contents of _den. """
        return self._den

    @property
    def float(self) -> float:
        """ Returns the float value. """
        return self._num/self._den

    @property
    def num_den_pair(self) -> tuple[int, int]:
        return self._num, self._den

    # 4. Methods
    # Logic commonly associated to data in this class.
    # Common operations on fractions,
    # standard ways to display fractions, etc.

    # 4(a). Public methods

    def neg(self) -> Frac:
        return Frac(-self._num, self._den)

    def add(self, other: Frac) -> Frac:
        sn, sd = self.num_den_pair
        on, od = other.num_den_pair
        return Frac(sn*od+sd*on, sd*od)

    def sub(self, other: Frac) -> Frac:
        # (Marginally) more efficient, less maintainable:
        # sn, sd = self.num_den_pair
        # on, od = other.num_den_pair
        # return Frac(sn*od-sd*on, sd*od)
        #
        # Answer using delegation of responsibility:
        return self.add(other.neg())

    def mult(self, other: Frac) -> Frac:
        return Frac(
            self._num*other._num,
            self._den*other._den
        )

    def div(self, other: Frac) -> Frac:
        if other == 0: # exploiting our __eq__ implementation!
            raise ZeroDivisionError()
        return Frac(
            self._num*other._den,
            self._den*other._num
        )

    # 4(b). Dunder methods (aka special methods)

    def __eq__(self, other: Any) -> bool:
        #                   ^^^ in __eq__, Any is legitimate
        """
        Special method implementing the result of == testing.
        """
        if isinstance(other, int) and self._den == 1:
            return self._num == other
            # This works because the implementation of int.__eq__
            # returns NotImplemented.
            # Otherwise, we'd have that
            #   Frac(2, 1) == 2 is True
            #   2 == Frac(2, 1) is False
        if not isinstance(other, Frac):
            # return False # Wrong thing to return for binary operators!
            # At some point, someone might implement a Decimal class
            # They might want it to interoperate with our Frac class
            # They might want to define equality with our Frac class
            # ... and returning False makes that impossible.
            return NotImplemented # the correct way to return False in __eq__
        sn, sd = self._num, self._den
        on, od = other._num, other._den
        sg, og = gcd(sn, sd), gcd(on, od)
        return sn//sg == on//og and sd//sg == od//og
        #                       ^^^ boolean operator
        # 'and', 'or', 'not' are bool operators
        # 'and' and 'or' are short-circuited
        # they are NOT implemented by a special method
        # they cannot be overridden :S

    def __repr__(self) -> str:
        """
        Special method meant to return a representation of the instance
        for development purposes. It should be as precise as possible.

        Ideally, it should be Python code which, if executed, would create
        an instance equal to this one.

        If not explicitly implemented but __str__ is implemented,
        it defaults to __str__.
        """
        return f"Frac({self._num}, {self._den})"

    def __str__(self) -> str:
        """
        Special method meant to return a pretty string representation
        of the instance. It need not be precise.

        If not explicitly implemented, defaults to __repr__.
        """
        if self._den == 1:
            return str(self._num)
            #      ^^^ builtin function calling __str__ under the hood
        return f"{self._num}/{self._den}"


    assert "Frac" not in dir() # True: Frac has not been defined yet

assert "Frac" in dir() # True: Frac has been defined once we left its scope

# print("  In frac_v1.py, just after Frac")
print(f"  In frac_v1.py, {Frac = }")

ZERO: Final[Frac] = Frac(0, 1)
ONE: Final[Frac] = Frac(1, 1)
PI: Final[Frac] = Frac(22, 7)
"""
A constant. Marked as Final, so it cannot be reassigned,
but the UPPER name already says that as a convention.
"""
