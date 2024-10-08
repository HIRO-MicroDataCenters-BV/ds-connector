from typing import Any

from abc import ABC, abstractmethod


class IQuery(ABC):
    """Interface for implementing repository queries"""

    @abstractmethod
    def build(self) -> dict[str, Any]:
        ...

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.build()})"


class GetByID(IQuery):
    _id: str

    def __init__(self, id: str) -> None:
        self._id = id

    def build(self) -> dict[str, str]:
        return {"id": self._id}


class GetPaginated(IQuery):
    _page: int
    _size: int

    def __init__(self, page: int, size: int) -> None:
        self._page = page
        self._size = size

    def build(self) -> dict[str, int]:
        return {"page": self._page, "size": self._size}
