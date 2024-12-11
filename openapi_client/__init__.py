# coding: utf-8

# flake8: noqa

"""
    OpenAPI3Definition 62

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.default_api import DefaultApi

# import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiAttributeError
from openapi_client.exceptions import ApiException

# import models into sdk package
from openapi_client.models.album import Album
from openapi_client.models.albums import Albums
from openapi_client.models.artist import Artist
from openapi_client.models.artists import Artists
from openapi_client.models.creator import Creator
from openapi_client.models.error import Error
from openapi_client.models.exception import Exception
from openapi_client.models.genre import Genre
from openapi_client.models.genres import Genres
from openapi_client.models.playlist import Playlist
from openapi_client.models.playlist_tracks import PlaylistTracks
from openapi_client.models.top_tracks import TopTracks
from openapi_client.models.track import Track
from openapi_client.models.tracks import Tracks
