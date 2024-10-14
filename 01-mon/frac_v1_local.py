"""
Class is data + logic
Python is very bad for comparing fractions. It is not accurately stored
"""

class Frac:
    """
    A class for immutable fractions
    """

    # == Data ==
    # Attributes = places where data is stored (keys in a dictionary)
    _num: Final[int] # static type check

    _den: Final[int]