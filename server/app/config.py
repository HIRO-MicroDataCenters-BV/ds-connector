from .core.connectors import IConnector
from .core.connectors.dummy import DummyConnector

CONNECTORS: list[IConnector] = [
    DummyConnector("connector1"),
]
