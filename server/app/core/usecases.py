from typing import cast

from .entities import DataProduct
from .queries import IQuery
from .repository import get_repository


async def get_data_products_list(query: IQuery | None = None) -> list[DataProduct]:
    result = await get_repository().list(query)
    return cast(list[DataProduct], result)


async def get_data_product(
    connector_id: str, query: IQuery | None = None
) -> DataProduct:
    result = await get_repository().get(connector_id, query)
    return cast(DataProduct, result)
