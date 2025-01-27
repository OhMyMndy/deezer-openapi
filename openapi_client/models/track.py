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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.artist import Artist
from typing import Optional, Set
from typing_extensions import Self

class Track(BaseModel):
    """
    Track
    """ # noqa: E501
    id: Optional[StrictInt] = None
    readable: Optional[StrictBool] = None
    title: Optional[StrictStr] = None
    title_short: Optional[StrictStr] = None
    title_version: Optional[StrictStr] = None
    irsc: Optional[StrictStr] = None
    link: Optional[StrictStr] = None
    duration: Optional[StrictInt] = None
    rank: Optional[StrictInt] = None
    explicit_lyrics: Optional[StrictBool] = None
    explicit_content_lyrics: Optional[StrictInt] = None
    explicit_content_cover: Optional[StrictInt] = None
    preview: Optional[StrictStr] = None
    md5_image: Optional[StrictStr] = None
    time_add: Optional[StrictInt] = None
    type: Optional[StrictStr] = None
    artist: Optional[Artist] = None
    album: Optional[Album] = None
    __properties: ClassVar[List[str]] = ["id", "readable", "title", "title_short", "title_version", "irsc", "link", "duration", "rank", "explicit_lyrics", "explicit_content_lyrics", "explicit_content_cover", "preview", "md5_image", "time_add", "type", "artist", "album"]

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
        """Create an instance of Track from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of album
        if self.album:
            _dict['album'] = self.album.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Track from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "readable": obj.get("readable"),
            "title": obj.get("title"),
            "title_short": obj.get("title_short"),
            "title_version": obj.get("title_version"),
            "irsc": obj.get("irsc"),
            "link": obj.get("link"),
            "duration": obj.get("duration"),
            "rank": obj.get("rank"),
            "explicit_lyrics": obj.get("explicit_lyrics"),
            "explicit_content_lyrics": obj.get("explicit_content_lyrics"),
            "explicit_content_cover": obj.get("explicit_content_cover"),
            "preview": obj.get("preview"),
            "md5_image": obj.get("md5_image"),
            "time_add": obj.get("time_add"),
            "type": obj.get("type"),
            "artist": Artist.from_dict(obj["artist"]) if obj.get("artist") is not None else None,
            "album": Album.from_dict(obj["album"]) if obj.get("album") is not None else None
        })
        return _obj

from openapi_client.models.album import Album
# TODO: Rewrite to not use raise_errors
Track.model_rebuild(raise_errors=False)

