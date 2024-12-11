# coding: utf-8

"""
    OpenAPI3Definition 62

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Artist(BaseModel):
    """
    Artist
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    link: Optional[StrictStr] = None
    picture: Optional[StrictStr] = None
    picture_small: Optional[StrictStr] = None
    picture_medium: Optional[StrictStr] = None
    picture_big: Optional[StrictStr] = None
    picture_xl: Optional[StrictStr] = None
    tracklist: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    artist: Optional[Artist] = None
    __properties: ClassVar[List[str]] = ["id", "name", "link", "picture", "picture_small", "picture_medium", "picture_big", "picture_xl", "tracklist", "type", "artist"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Artist from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of artist
        if self.artist:
            _dict['artist'] = self.artist.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Artist from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "link": obj.get("link"),
            "picture": obj.get("picture"),
            "picture_small": obj.get("picture_small"),
            "picture_medium": obj.get("picture_medium"),
            "picture_big": obj.get("picture_big"),
            "picture_xl": obj.get("picture_xl"),
            "tracklist": obj.get("tracklist"),
            "type": obj.get("type"),
            "artist": Artist.from_dict(obj["artist"]) if obj.get("artist") is not None else None
        })
        return _obj

# TODO: Rewrite to not use raise_errors
Artist.model_rebuild(raise_errors=False)

