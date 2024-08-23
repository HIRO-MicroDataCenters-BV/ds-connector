from .connectors import IConnector
from .exceptions import ConnectorAlreadyExists, ConnectorNotFound


class ConnectorsManager:
    _connectors: dict[str, IConnector]

    def __init__(self):
        self._connectors = {}

    @property
    def connectors(self) -> list[IConnector]:
        return list(self._connectors.values())

    def get(self, id: str) -> IConnector:
        if id not in self._connectors:
            raise ConnectorNotFound
        return self._connectors[id]

    def register(self, connector: IConnector) -> None:
        if connector.id in self._connectors:
            raise ConnectorAlreadyExists
        self._connectors[connector.id] = connector

    def unregister(self, connector: IConnector) -> None:
        connector_ = self.get(connector.id)
        del self._connectors[connector_.id]
