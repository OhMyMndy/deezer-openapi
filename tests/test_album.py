import unittest
from . import ApiTest, ALBUM_ID

from pprint import pprint


class TestAlbum(ApiTest):
    def testAlbum(self):
        album = self.api_instance.get_album(ALBUM_ID)
        if "error" not in album:
            print(album.to_json())


if __name__ == "__main__":
    unittest.main()
