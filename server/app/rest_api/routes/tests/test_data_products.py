import pytest
from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from pytest_mock import MockerFixture

from app.core import init_repository
from app.core.connectors import IConnector
from app.core.entities import DataProduct as DataProductEntity
from app.core.exceptions import ConnectorNotFound, DataProductNotFound
from app.core.repository import Repository
from app.core.tests.fabrics import create_connector, create_dataproduct
from app.rest_api.models import DataProduct, PaginatedResult
from app.rest_api.strings import CONNECTOR_NOT_FOUND, DATA_PRODUCT_NOT_FOUND

from .. import data_products


@pytest.mark.usefixtures("mocker")
class TestItemRoutes:
    @pytest.fixture
    def data_products(self) -> list[DataProductEntity]:
        return [
            create_dataproduct(id="dataproduct1"),
            create_dataproduct(id="dataproduct2"),
        ]

    @pytest.fixture
    def connector(self, data_products: list[DataProductEntity]) -> IConnector:
        return create_connector(data_products=data_products)

    @pytest.fixture
    def repository(self, connector: IConnector) -> Repository:
        return init_repository([connector])

    @pytest.fixture
    def client(self) -> TestClient:
        app = FastAPI()
        app.include_router(data_products.routes.router)
        return TestClient(app)

    def test_get_data_products(
        self,
        client: TestClient,
        data_products: list[DataProductEntity],
        repository: Repository,
    ) -> None:
        response = client.get("/data-products/")
        assert response.status_code == status.HTTP_200_OK

        items = [DataProduct.from_entity(item) for item in data_products]
        expected = PaginatedResult(page=1, size=100, items=items)
        assert response.json() == expected.model_dump(by_alias=True)

    def test_get_data_product(
        self,
        client: TestClient,
        data_products: list[DataProductEntity],
        connector: IConnector,
        repository: Repository,
    ) -> None:
        data_product = data_products[0]
        response = client.get(f"/data-products/{connector.id}/{data_product.id}/")
        assert response.status_code == 200

        expected_item = DataProduct.from_entity(data_product)
        assert response.json() == expected_item.model_dump(by_alias=True)

    def test_get_data_product_if_connector_not_found(
        self,
        mocker: MockerFixture,
        client: TestClient,
        repository: Repository,
    ) -> None:
        mock_get_data_product = mocker.patch("app.core.usecases.get_data_product")
        mock_get_data_product.side_effect = ConnectorNotFound

        response = client.get("/data-products/connector_id/product_id/")
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json()["detail"] == CONNECTOR_NOT_FOUND

    def test_get_data_product_if_data_product_not_found(
        self,
        mocker: MockerFixture,
        client: TestClient,
        repository: Repository,
    ) -> None:
        mock_get_data_product = mocker.patch("app.core.usecases.get_data_product")
        mock_get_data_product.side_effect = DataProductNotFound

        response = client.get("/data-products/connector_id/product_id/")
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json()["detail"] == DATA_PRODUCT_NOT_FOUND
