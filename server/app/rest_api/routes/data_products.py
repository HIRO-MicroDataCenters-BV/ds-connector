from typing import Any, Callable

from enum import Enum

from classy_fastapi import Routable, get
from fastapi import HTTPException

from app.core import queries, usecases
from app.core.exceptions import ConnectorNotFound, DataProductNotFound

from ..models import DataProduct, PaginatedResult
from ..strings import CONNECTOR_NOT_FOUND, DATA_PRODUCT_NOT_FOUND

TAGS: list[str | Enum] = ["Data product"]


UseCasesType = dict[str, Callable[..., Any]]


class DataProductRoutes(Routable):
    _usecases: UseCasesType

    def __init__(self, usecases: UseCasesType) -> None:
        self._usecases = usecases
        super().__init__()

    @get(
        "/data-products/",
        operation_id="get_data_products",
        summary="Get a list of data products",
        response_model=PaginatedResult,
        tags=TAGS,
    )
    async def get_data_products(
        self,
        page: int = 1,
        pageSize: int = 100,
    ) -> PaginatedResult:
        """Returns a list of data products with the ability to paginate"""
        query = queries.GetPaginated(page=page, size=pageSize)
        data_products = await self._usecases["list"](query)
        items = [DataProduct.from_entity(item) for item in data_products]
        return PaginatedResult(page=page, size=pageSize, items=items)

    @get(
        "/data-products/{connector_id}/{data_product_id}/",
        operation_id="get_data_product",
        summary="Get a data product details",
        response_model=DataProduct,
        tags=TAGS,
    )
    async def get_data_product(
        self,
        connector_id: str,
        data_product_id: str,
    ) -> DataProduct:
        """Returns an information about the data product"""
        try:
            data_product = await self._usecases["get"](
                connector_id, queries.GetByID(data_product_id)
            )
        except ConnectorNotFound:
            raise HTTPException(status_code=404, detail=CONNECTOR_NOT_FOUND)
        except DataProductNotFound:
            raise HTTPException(status_code=404, detail=DATA_PRODUCT_NOT_FOUND)
        return DataProduct.from_entity(data_product)


routes = DataProductRoutes(
    usecases={
        "list": usecases.get_data_products_list,
        "get": usecases.get_data_product,
    }
)
