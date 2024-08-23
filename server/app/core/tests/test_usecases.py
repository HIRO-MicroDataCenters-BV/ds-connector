import pytest

from ..repository import init_repository
from ..usecases import get_data_product, get_data_products_list
from .fabrics import create_connector, create_dataproduct, create_query


class TestDataProductUsecases:
    @pytest.fixture
    def data_products(self):
        return [
            create_dataproduct(id="dataproduct1"),
            create_dataproduct(id="dataproduct2"),
        ]

    @pytest.mark.asyncio
    async def test_get_data_products_list(self, data_products):
        connector = create_connector(data_products=data_products)
        init_repository([connector])
        query = create_query()
        result = await get_data_products_list(query)
        assert set([item.id for item in result]) == set(
            [item.id for item in data_products]
        )

    @pytest.mark.asyncio
    async def test_get_data_product(self, data_products):
        connector = create_connector(data_products=data_products)
        init_repository([connector])
        query = create_query()
        result = await get_data_product(connector.id, query)
        assert result == data_products[0]
