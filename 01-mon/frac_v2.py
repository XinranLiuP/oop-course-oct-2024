"""
A better implementation of fractions, with more bells and whistles.
"""

from __future__ import annotations
from math import gcd
from typing import Any, ClassVar

class Frac:

    PI: ClassVar[Frac] # can't set it here because Frac doesn't exist yet.

    @staticmethod
    def from_int(num: int) -> Frac:
        """
        Utility/alternative constructor,
        to build fractions from integers.

        A static method is a method on the class object Frac.
        Called as Frac.from_int(...) rather than Frac(22, 7).from_int(...).
        """
        return Frac(num, 1)

    @staticmethod
    def from_str(frac: str) -> Frac:
        """
        Utility/alternative constructor,
        to build fractions from str representation.
        """
        if "/" not in frac:
            return Frac.from_int(int(frac))
            #  parses str -> int ^^^^^^^^^
        num_str, den_str = frac.split("/")
        return Frac(int(num_str), int(den_str))
        # Three different stages of validation at play here:
        # 1. destructuring raises ValueError if "/" appears > 1
        # 2. int(...) raise ValueError if not int representation of num and den
        # 3. Frac(..., ...) raises ZeroDivisionError if den == 0

    # Private attributes store the class data

    __num: int
    """ This stores the numerator. """

    __den: int
    """ This stores the denominator. """

    # Initialiser (still not a constructor)
    def __init__(self, num: int, den: int = 1) -> None:
        #                   default value ^^^
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
        g = gcd(num, den)
        num, den = num//g, den//g
        # 2. Setting attributes
        self.__num = num
        self.__den = den

    @property
    def num(self) -> int:
        """ The numerator of the fraction. """
        return self.__num

    @property
    def den(self) -> int:
        """ The denominator of the fraction. """
        return self.__den

    @property
    def num_den_pair(self) -> tuple[int, int]:
        return self.__num, self.__den

    def __neg__(self) -> Frac:
        """ Implements the unary operator - """
        return Frac(-self.num, self.den)

    def __add__(self, rhs: Frac|int) -> Frac:
        """ Implements the binary operator + """
        if isinstance(rhs, int):
            # other = Frac(other, 1)     # Option 1
            # other = Frac(other)        # Option 2, if den=1 in __init__
            rhs = Frac.from_int(rhs) # Option 3, utility constructor
        sn, sd = self.num_den_pair
        on, od = rhs.num_den_pair
        return Frac(sn*od+sd*on, sd*od)

    def __radd__(self, lhs: int) -> Frac:
        """
        Implements int+Frac
               lhs ^^^ ^^^^ self
        """
        return Frac.from_int(lhs)+self

    def __sub__(self, rhs: Frac|int) -> Frac:
        """ Implements the binary operator - """
        return self+(-rhs)

    def __rsub__(self, lhs: int) -> Frac:
        """
        Implements int-Frac
               lhs ^^^ ^^^^ self
        """
        return Frac.from_int(lhs)-self

    def __mul__(self, rhs: Frac|int) -> Frac:
        """ Implements the binary operator * """
        if isinstance(rhs, int):
            rhs = Frac.from_int(rhs)
        return Frac(self.num*rhs.num, self.den*rhs.den)

    def __rmul__(self, lhs: int) -> Frac:
        """
        Implements int*Frac
               lhs ^^^ ^^^^ self
        """
        return Frac.from_int(lhs)*self

    def __truediv__(self, rhs: Frac) -> Frac:
        """
        Implements the binary operator /
        __floordiv__ implements the binary operator //
        """
        if rhs == 0: # exploiting our __eq__ implementation!
            raise ZeroDivisionError()
        if isinstance(rhs, int):
            rhs = Frac.from_int(rhs)
        return Frac(self.num*rhs.den,self.den*rhs.num
        )

    def __rtruediv__(self, lhs: int) -> Frac:
        """
        Implements int/Frac
               lhs ^^^ ^^^^ self
        """
        return Frac.from_int(lhs)/self

    def __eq__(self, other: Any) -> bool:
        """
        The contract for __eq__ and __hash__ is that:

        x == y must imply hash(x) == hash(y)

        If we redefine __eq__, we must explicitly redefine __hash__,
        and ensure that the above holds.

        The default implementation of __eq__ is:

        def __eq__(self, other: Any) -> bool:
            return self is other
            #           ^^ identity, literally the same pointer

        Necessarily, equality implies equal hash with this implementation.
        """
        if isinstance(other, int) and self.den == 1:
            return self.num == other
        if not isinstance(other, Frac):
            return NotImplemented
        return self.num == other.num and self.den == other.den

    def __hash__(self) -> int:
        """
        To ensure that this respects the requirements,
        derive the hash from data which uniquely identifies a Frac instance.
        """
        if self.den == 1:
            return hash(self.num)
        return hash((self.num, self.den))

    def __repr__(self) -> str:
        return f"Frac({self.num}, {self.den})"

    def __str__(self) -> str:
        if self.den == 1:
            return str(self.num)
        return f"{self.num}/{self.den}"

Frac.PI = Frac(22, 7)
