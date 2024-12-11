PLAYLIST_ID = 13235845183
ALBUM_ID = 450307185
ARTIST_ID = 3621331

import openapi_client
import unittest


class ApiTest(unittest.TestCase):
    def setUp(self):
        configuration = openapi_client.Configuration(
            host="https://api.deezer.com/", debug=False
        )

        api_client = openapi_client.ApiClient(configuration)
        self.api_instance = openapi_client.DefaultApi(api_client)
