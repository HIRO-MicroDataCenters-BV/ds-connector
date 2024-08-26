import pytest

from ..dummy import DUMMY_DATA, DummyConnector
from ..interface import IConnector


class TestDummyConnector:
    @pytest.fixture
    def connector(self) -> IConnector:
        return DummyConnector(id="test_connector_id")

    @pytest.mark.asyncio
    async def test_list(self, connector: IConnector) -> None:
        result = await connector.list()
        assert result == DUMMY_DATA

    @pytest.mark.asyncio
    async def test_get(self, connector: IConnector) -> None:
        result = await connector.get()
        assert result == DUMMY_DATA[0]
