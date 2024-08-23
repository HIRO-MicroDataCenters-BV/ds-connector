import pytest

from ..repository import Repository, get_repository, init_repository
from .fabrics import create_connector, create_dataproduct, create_manager, create_query


class TestRepository:
    @pytest.mark.asyncio
    async def test_list(self):
        items = [
            create_dataproduct(id="dataproduct1"),
            create_dataproduct(id="dataproduct2"),
            create_dataproduct(id="dataproduct3"),
            create_dataproduct(id="dataproduct4"),
        ]
        connector1 = create_connector(id="connector1", data_products=items[:2])
        connector2 = create_connector(id="connector2", data_products=items[2:])
        manager = create_manager([connector1, connector2])
        query = create_query()
        repository = Repository(manager)
        result = await repository.list(query)
        assert set([item.id for item in result]) == set([item.id for item in items])

    @pytest.mark.asyncio
    async def test_get(self):
        data_product = create_dataproduct()
        connector = create_connector(data_products=[data_product])
        manager = create_manager([connector])
        query = create_query()
        repository = Repository(manager)
        result = await repository.get(connector.id, query)
        assert result == data_product


class TestGlobalRepository:
    @pytest.mark.asyncio
    async def test_common(self):
        items = [
            create_dataproduct(id="dataproduct1"),
            create_dataproduct(id="dataproduct2"),
        ]
        connector = create_connector(data_products=items)
        repository = init_repository([connector])
        ret_repository = get_repository()
        assert repository == ret_repository
        result = await ret_repository.list()
        assert set([item.id for item in result]) == set([item.id for item in items])
