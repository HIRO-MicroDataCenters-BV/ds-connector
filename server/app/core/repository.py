import asyncio

from .connectors import IConnector
from .entities import DataProduct
from .exceptions import RepositoryIsNotInitialized
from .manager import ConnectorsManager
from .queries import IQuery


class Repository:
    """
    This class implements the logic of interaction with connectors through
    a single interface as with a single data source.

    """

    _connectors_manager: ConnectorsManager

    def __init__(self, connectors_manager):
        self._connectors_manager = connectors_manager

    async def list(self, query: IQuery | None = None) -> list[DataProduct]:
        """Getting list of data products"""
        tasks = [
            connector.list(query) for connector in self._connectors_manager.connectors
        ]
        results = await asyncio.gather(*tasks)
        return [item for sublist in results for item in sublist]

    async def get(
        self,
        connector_id: str,
        query: IQuery | None = None,
    ) -> DataProduct:
        """Getting one data product"""
        connector = self._connectors_manager.get(connector_id)
        return await connector.get(query)

    async def read(self, *args, **kwargs):
        """Getting real data from the data product"""
        # TODO: Implement later
        raise NotImplementedError

    async def write(self, *args, **kwargs):
        """Saving data on the partner side"""
        # TODO: Implement later
        raise NotImplementedError


global_repository: Repository | None = None


def init_repository(connectors: list[IConnector]) -> Repository:
    """Global repository initialization"""
    global global_repository
    manager = ConnectorsManager()
    for connector in connectors:
        manager.register(connector)
    global_repository = Repository(manager)
    return global_repository


def get_repository():
    """
    Get the global repository.
    Must be called after init_repository.

    """
    global global_repository
    if global_repository is None:
        raise RepositoryIsNotInitialized
    return global_repository
