import pytest

from ..exceptions import ConnectorAlreadyExists, ConnectorNotFound
from ..manager import ConnectorsManager
from .fabrics import create_connector


class TestConnectorsManager:
    def test_connectors_list(self):
        connector = create_connector()
        manager = ConnectorsManager()
        manager.register(connector)
        assert manager.connectors == [connector]

    def test_get_connector(self):
        connector = create_connector()
        manager = ConnectorsManager()
        manager.register(connector)

        result = manager.get(connector.id)

        assert result == connector

    def test_register(self):
        manager = ConnectorsManager()

        assert len(manager.connectors) == 0

        connector = create_connector()
        manager.register(connector)

        assert len(manager.connectors) == 1
        assert manager.connectors[0] == connector

    def test_register_if_connector_already_exists(self):
        connector = create_connector()
        manager = ConnectorsManager()
        manager.register(connector)

        with pytest.raises(ConnectorAlreadyExists):
            manager.register(connector)

    def test_unregister(self):
        connector = create_connector()
        manager = ConnectorsManager()
        manager.register(connector)

        assert len(manager.connectors) == 1

        manager.unregister(connector)

        assert len(manager.connectors) == 0

    def test_register_if_connector_not_found(self):
        connector = create_connector()
        manager = ConnectorsManager()

        with pytest.raises(ConnectorNotFound):
            manager.unregister(connector)
