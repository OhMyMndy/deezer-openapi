import unittest
from . import ApiTest, ARTIST_ID

from pprint import pprint
import json


class TestArtist(ApiTest):
    def testRelatedArtists(self):
        related_artists = self.api_instance.get_related_artists(ARTIST_ID)
        if "error" not in related_artists:
            pprint(json.loads(related_artists.to_json()))

    def testArtistTopTracks(self):
        top_tracks = self.api_instance.get_artist_top_tracks(ARTIST_ID)
        if "error" not in top_tracks:
            pprint(json.loads(top_tracks.to_json()))

    def testArtistRadio(self):
        radio_tracks = self.api_instance.get_artist_radio(ARTIST_ID)
        if "error" not in radio_tracks:
            pprint(json.loads(radio_tracks.to_json()))


if __name__ == "__main__":
    unittest.main()
