from ..entities import Connector, DataProduct, Interface, Tag
from .interface import IConnector

DUMMY_DATA = [
    DataProduct(
        id="dataproduct1",
        name="cancer_2020",
        size=1024,
        mimetype="text/plain",
        digest="1kf50e8ad219e34f0b911e097b7b588e31f9b435",
        tags=[
            Tag("tag1"),
        ],
        source={
            "connector": Connector("connector1"),
            "interface": Interface("interface1"),
        },
        _links={
            "accessPoint": "/connector1/interface1/dataproduct1/",
        },
    ),
    DataProduct(
        id="dataproduct2",
        name="cancer_2021",
        size=2048,
        mimetype="text/plain",
        digest="4gf50e8ad219e34f0b911e097b7b588e31f9b435",
        tags=[
            Tag("tag1"),
            Tag("tag2"),
        ],
        source={
            "connector": Connector("connector1"),
            "interface": Interface("interface1"),
        },
        _links={
            "accessPoint": "/connector1/interface1/dataproduct2/",
        },
    ),
    DataProduct(
        id="dataproduct3",
        name="cancer_2022",
        size=512,
        mimetype="application/json",
        digest="3sf50e8ad219e34f0b911e097b7b588e31f9b435",
        tags=[
            Tag("tag3"),
        ],
        source={
            "connector": Connector("connector2"),
        },
        _links={
            "accessPoint": "/connector2/dataproduct3/",
        },
    ),
]


class DummyConnector(IConnector):
    async def list(self, *args, **kwargs) -> list[DataProduct]:
        return DUMMY_DATA

    async def get(self, *args, **kwargs) -> DataProduct:
        return DUMMY_DATA[0]
