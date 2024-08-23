import pytest

from ..dummy import DUMMY_DATA, DummyConnector


class TestDummyConnector:
    @pytest.fixture
    def connector(self):
        return DummyConnector(id="test_connector_id")

    @pytest.mark.asyncio
    async def test_list(self, connector):
        result = await connector.list()
        assert result == DUMMY_DATA

    @pytest.mark.asyncio
    async def test_get(self, connector):
        result = await connector.get()
        assert result == DUMMY_DATA[0]
