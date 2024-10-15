from __future__ import annotations
from collections.abc import Iterable
from typing import Generic, Iterable, TypeVar

ItemT = TypeVar("ItemT") #Type variable for items of bag
#be carefull you are importing from typing
#need to write a name that is the same as the assigned to pass the static check
#because before assignment TypeVar does not know the name

class Bag(Generic[ItemT]):
    """
    """
    def __init__(self, items: Iterable[ItemT]) -> None: 
        #Advantage of ItemT over Any is to ensure all elements are the same type
        #ItemT is stored in mypy, not available at runtime
        raise NotImplementedError()