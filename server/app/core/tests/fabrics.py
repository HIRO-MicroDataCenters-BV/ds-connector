from ..connectors import IConnector
from ..entities import Connector, DataProduct, Interface, Tag
from ..manager import ConnectorsManager
from ..queries import IQuery


def create_dataproduct(**kwargs) -> DataProduct:
    data = {
        "id": "dataproduct1",
        "name": "cancer_2020",
        "size": 1024,
        "mimetype": "text/plain",
        "digest": "1df50e8ad219e34f0b911e097b7b588e31f9b435",
        "tags": [
            Tag("tag1"),
        ],
        "source": {
            "connector": Connector("connector1"),
            "interface": Interface("interface1"),
        },
        "_links": {
            "accessPoint": "/connector1/interface1/dataproduct1/",
        },
    }
    data.update(kwargs)
    return DataProduct(**data)  # type: ignore


def create_query(result_dict: dict | None = None) -> IQuery:
    class FakeQuery(IQuery):
        def build(self):
            return result_dict if result_dict is not None else {}

    return FakeQuery()


def create_connector(
    id="test_connector_id",
    data_products: list[DataProduct] | None = None,
) -> IConnector:
    items = [] if data_products is None else data_products

    class FakeConnector(IConnector):
        async def list(self, *args, **kwargs) -> list[DataProduct]:
            return items

        async def get(self, *args, **kwargs) -> DataProduct:
            return items[0]

    return FakeConnector(id=id)


def create_manager(connectors: list[IConnector] | None = None) -> ConnectorsManager:
    if connectors is None:
        connectors = []
    manager = ConnectorsManager()
    for connector in connectors:
        manager.register(connector)
    return manager
