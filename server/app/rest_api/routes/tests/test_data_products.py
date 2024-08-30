from typing import Callable

from fastapi import FastAPI, status
from fastapi.routing import APIRouter
from fastapi.testclient import TestClient

from app.core.entities import DataProduct as DataProductEntity
from app.core.exceptions import ConnectorNotFound, DataProductNotFound
from app.core.queries import GetByID, GetPaginated, IQuery
from app.core.tests.fabrics import create_dataproduct
from app.rest_api.models import DataProduct, PaginatedResult
from app.rest_api.strings import CONNECTOR_NOT_FOUND, DATA_PRODUCT_NOT_FOUND

from ..data_products import DataProductRoutes, IDataProductUsecases


def create_client(router: APIRouter) -> TestClient:
    app = FastAPI()
    app.include_router(router)
    return TestClient(app)


def create_usecases(
    list_usecase: Callable[..., list[DataProductEntity]] | None = None,
    get_usecase: Callable[..., DataProductEntity] | None = None,
) -> IDataProductUsecases:
    class Usecases(IDataProductUsecases):
        async def list(
            self,
            query: IQuery | None = None,
        ) -> list[DataProductEntity]:
            if list_usecase is None:
                raise NotImplementedError
            return list_usecase(query)

        async def get(
            self, connector_id: str, query: IQuery | None = None
        ) -> DataProductEntity:
            if get_usecase is None:
                raise NotImplementedError
            return get_usecase(connector_id, query)

    return Usecases()


class TestItemRoutes:
    def test_get_data_products(self) -> None:
        data_products = [
            create_dataproduct(id="dataproduct1"),
            create_dataproduct(id="dataproduct2"),
        ]

        def list_usecase(query: GetPaginated) -> list[DataProductEntity]:
            assert query.build() == {"page": 1, "size": 100}
            return data_products

        usecases = create_usecases(list_usecase=list_usecase)
        routes = DataProductRoutes(usecases=usecases)

        client = create_client(routes.router)
        response = client.get("/data-products/")
        assert response.status_code == status.HTTP_200_OK

        items = [DataProduct.from_entity(item) for item in data_products]
        expected = PaginatedResult(page=1, size=100, items=items)
        assert response.json() == expected.model_dump(by_alias=True)

    def test_get_data_product(self) -> None:
        connector_id_ = "connector1"
        data_product = create_dataproduct()

        def get_usecase(connector_id: str, query: GetByID) -> DataProductEntity:
            assert connector_id == connector_id_
            assert query.build() == {"id": data_product.id}
            return data_product

        usecases = create_usecases(get_usecase=get_usecase)
        routes = DataProductRoutes(usecases=usecases)

        client = create_client(routes.router)
        response = client.get(f"/data-products/{connector_id_}/{data_product.id}/")
        assert response.status_code == 200

        expected_item = DataProduct.from_entity(data_product)
        assert response.json() == expected_item.model_dump(by_alias=True)

    def test_get_data_product_if_connector_not_found(self) -> None:
        def get_usecase(
            connector_id: str,
            query: IQuery | None = None,
        ) -> DataProductEntity:
            raise ConnectorNotFound

        usecases = create_usecases(get_usecase=get_usecase)
        routes = DataProductRoutes(usecases=usecases)

        client = create_client(routes.router)
        response = client.get("/data-products/connector_id/product_id/")
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json()["detail"] == CONNECTOR_NOT_FOUND

    def test_get_data_product_if_data_product_not_found(self) -> None:
        def get_usecase(
            connector_id: str,
            query: IQuery | None = None,
        ) -> DataProductEntity:
            raise DataProductNotFound

        usecases = create_usecases(get_usecase=get_usecase)
        routes = DataProductRoutes(usecases=usecases)

        client = create_client(routes.router)
        response = client.get("/data-products/connector_id/product_id/")
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json()["detail"] == DATA_PRODUCT_NOT_FOUND
