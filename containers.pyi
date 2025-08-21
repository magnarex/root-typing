from typing import TypeVar, Generic, Iterable, overload

from numpy import float64 as RDouble, float32 as RFloat
from numpy.typing import NDArray

from .core import TObject

ArrayType = TypeVar('ContentType', RDouble, RFloat)
ContentType = TypeVar('ObjectType', bound='TObject')

class TCollection(TObject, Iterable[ContentType]):
    pass

class TSeqCollection(TCollection[ContentType]):
    pass

class TArray(Generic[ArrayType]):
    def GetArray(self) -> NDArray[ArrayType]:
        """
        Return the array.
        """
        ...

class TArrayD(TArray[RDouble]):
    pass

class TArrayF(TArray[RFloat]):
    pass

class TList(TSeqCollection[ContentType]):
    @overload
    def FindObject(self, name: str) -> ContentType:
        """
        Find an object in this list using its name.

        Requires a sequential scan till the object has been found.
        Returns 0 if object with specified name is not found. This
        method overrides the generic FindObject() of TCollection for efficiency reasons.
        """
        ...
    