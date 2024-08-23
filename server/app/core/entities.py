from typing import Literal

from dataclasses import dataclass


@dataclass
class Tag:
    text: str


@dataclass
class Connector:
    id: str


@dataclass
class Interface:
    id: str


@dataclass
class DataProduct:
    id: str
    name: str
    size: int
    mimetype: str
    digest: str
    tags: list[Tag]
    source: dict[Literal["connector"] | Literal["interface"], Connector | Interface]
    _links: dict[Literal["accessPoint"], str]
