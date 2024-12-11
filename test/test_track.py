# coding: utf-8

"""
    OpenAPI3Definition 62

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.track import Track

class TestTrack(unittest.TestCase):
    """Track unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Track:
        """Test Track
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Track`
        """
        model = Track()
        if include_optional:
            return Track(
                id = 56,
                readable = True,
                title = '',
                title_short = '',
                title_version = '',
                irsc = '',
                link = '',
                duration = 56,
                rank = 56,
                explicit_lyrics = True,
                explicit_content_lyrics = 56,
                explicit_content_cover = 56,
                preview = '',
                md5_image = '',
                time_add = 56,
                type = '',
                artist = openapi_client.models.artist.Artist(
                    id = 56, 
                    name = '', 
                    link = '', 
                    picture = '', 
                    picture_small = '', 
                    picture_medium = '', 
                    picture_big = '', 
                    picture_xl = '', 
                    tracklist = '', 
                    type = '', 
                    artist = openapi_client.models.artist.Artist(
                        id = 56, 
                        name = '', 
                        link = '', 
                        picture = '', 
                        picture_small = '', 
                        picture_medium = '', 
                        picture_big = '', 
                        picture_xl = '', 
                        tracklist = '', 
                        type = '', ), ),
                album = openapi_client.models.album.Album(
                    id = 56, 
                    title = '', 
                    upc = '', 
                    cover = '', 
                    cover_small = '', 
                    cover_medium = '', 
                    cover_big = '', 
                    cover_xl = '', 
                    md5_image = '', 
                    tracklist = '', 
                    type = '', 
                    genre_id = 56, 
                    genres = openapi_client.models.genres.Genres(
                        data = [
                            openapi_client.models.genre.Genre(
                                id = 56, 
                                name = '', 
                                picture = '', 
                                type = '', )
                            ], ), 
                    label = '', 
                    nb_tracks = 56, 
                    duration = 56, 
                    fans = 56, 
                    release_date = '', 
                    record_type = '', 
                    available = True, 
                    explicit_lyrics = True, 
                    explicit_content_lyrics = 56, 
                    explicit_content_cover = 56, 
                    contributors = [
                        openapi_client.models.artist.Artist(
                            id = 56, 
                            name = '', 
                            link = '', 
                            picture = '', 
                            picture_small = '', 
                            picture_medium = '', 
                            picture_big = '', 
                            picture_xl = '', 
                            tracklist = '', 
                            type = '', 
                            artist = openapi_client.models.artist.Artist(
                                id = 56, 
                                name = '', 
                                link = '', 
                                picture = '', 
                                picture_small = '', 
                                picture_medium = '', 
                                picture_big = '', 
                                picture_xl = '', 
                                tracklist = '', 
                                type = '', ), )
                        ], 
                    artist = , 
                    tracks = openapi_client.models.tracks.Tracks(), )
            )
        else:
            return Track(
        )
        """

    def testTrack(self):
        """Test Track"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
