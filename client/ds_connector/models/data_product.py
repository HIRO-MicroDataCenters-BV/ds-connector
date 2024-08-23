# coding: utf-8

"""
    Data Space Connector service

    This connector requests data from the data layer and provides a REST API for servicing requests from the catalog service.

    The version of the OpenAPI document: 0.1.0
    Contact: all-hiro@hiro-microdatacenters.nl
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from ds_connector.models.tag import Tag
from typing import Optional, Set
from typing_extensions import Self

class DataProduct(BaseModel):
    """
    DataProduct
    """ # noqa: E501
    id: StrictStr
    name: StrictStr
    size: StrictInt
    mimetype: StrictStr
    digest: StrictStr
    tags: List[Tag]
    source: Dict[str, Any]
    links: Dict[str, StrictStr] = Field(alias="_links")
    __properties: ClassVar[List[str]] = ["id", "name", "size", "mimetype", "digest", "tags", "source", "_links"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DataProduct from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item in self.tags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tags'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataProduct from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "size": obj.get("size"),
            "mimetype": obj.get("mimetype"),
            "digest": obj.get("digest"),
            "tags": [Tag.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "source": obj.get("source"),
        })
        return _obj


