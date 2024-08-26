from typing import Literal

import dataclasses

from pydantic import BaseModel, Field

from app.core.entities import DataProduct as DataProductEntity


class HealthCheck(BaseModel):
    status: str = Field(examples=["OK"])


class Tag(BaseModel):
    text: str = Field(examples=["tag1"])


class Connector(BaseModel):
    id: str = Field(examples=["connector1"])


class Interface(BaseModel):
    id: str = Field(examples=["interface1"])


class DataProduct(BaseModel):
    id: str
    name: str
    size: int
    mimetype: str
    digest: str
    tags: list[Tag]
    source: dict[Literal["connector"] | Literal["interface"], Connector | Interface]
    links: dict[Literal["accessPoint"], str] = Field(alias="_links")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "8D8AC610-566D-4EF0-9C22-186B2A5ED793",
                    "name": "cancer_data_2024",
                    "size": 1024,
                    "mimetype": "text/plain",
                    "digest": "1df50e8ad219e34f0b911e097b7b588e31f9b435",
                    "tags": [
                        {
                            "text": "tag1",
                        }
                    ],
                    "source": {
                        "connector": {
                            "id": "connector1",
                        },
                        "interface": {
                            "id": "interface1",
                        },
                    },
                    "_links": {
                        "accessPoint": "/connector1/interface1/"
                        "8D8AC610-566D-4EF0-9C22-186B2A5ED793/",
                    },
                }
            ]
        }
    }

    @classmethod
    def from_entity(cls, entity: DataProductEntity) -> "DataProduct":
        return cls(**dataclasses.asdict(entity))


class PaginatedResult(BaseModel):
    page: int = Field(examples=[1])
    size: int = Field(examples=[100])
    items: list[DataProduct]
