import unittest
from . import ApiTest, PLAYLIST_ID
from pprint import pprint


class TestPlaylist(ApiTest):
    def testPlaylist(self):
        api_response = self.api_instance.get_playlist_tracks(PLAYLIST_ID)
        if "error" not in api_response:
            for track in api_response.data:
                pprint(track)


if __name__ == "__main__":
    unittest.main()
