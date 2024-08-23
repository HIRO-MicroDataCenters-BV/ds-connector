import io
from abc import ABC, abstractmethod

from ..entities import DataProduct
from ..queries import IQuery


class IConnector(ABC):
    _id: str

    def __init__(self, id: str) -> None:
        self._id = id

    @property
    def id(self):
        return self._id

    @abstractmethod
    async def list(self, query: IQuery | None = None) -> list[DataProduct]:
        ...

    @abstractmethod
    async def get(self, query: IQuery | None = None) -> DataProduct:
        ...

    async def read(self, data_product: DataProduct) -> io.BytesIO:
        raise NotImplementedError

    async def write(self, data_product: DataProduct, data: io.BytesIO) -> None:
        raise NotImplementedError
