import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
import json

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(host="https://api.deezer.com/", debug=True)


playlist_id = 13235845183
album_id = 450307185
artist_id = 3621331


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    index = None  # int |  (optional)

    # try:
    #     api_response = api_instance.get_playlist_tracks(id, index=index)
    #     print("The response of DefaultApi->get_playlist_tracks:\n")
    #     if api_response.error is None:
    #         for track in api_response.data:
    #             pprint(track)
    # except ApiException as e:
    #     print("Exception when calling DefaultApi->get_playlist_tracks: %s\n" % e)
    #

    # api_response = api_instance.get_playlist(playlist_id)
    # if "error" not in api_response:
    #     for track in api_response.tracks.data:
    #         pprint(track)

    # album = api_instance.get_album(album_id)
    # if "error" not in album:
    #     print(album.to_json())
    # artist = api_instance.get_album(artist_id)
    # if "error" not in artist:
    #     pprint(json.loads(artist.to_json()))

    # top_tracks = api_instance.get_artist_top_tracks(artist_id)
    # if "error" not in top_tracks:
    #     pprint(json.loads(top_tracks.to_json()))

    # related_artists = api_instance.get_related_artists(artist_id)
    # if "error" not in related_artists:
    #     pprint(json.loads(related_artists.to_json()))

    radio_tracks = api_instance.get_artist_radio(artist_id)
    if "error" not in radio_tracks:
        pprint(json.loads(radio_tracks.to_json()))
