# PlaylistTracks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** |  | [optional] 
**data** | [**List[Track]**](Track.md) |  | [optional] 
**error** | [**Exception**](Exception.md) |  | [optional] 

## Example

```python
from openapi_client.models.playlist_tracks import PlaylistTracks

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistTracks from a JSON string
playlist_tracks_instance = PlaylistTracks.from_json(json)
# print the JSON string representation of the object
print(PlaylistTracks.to_json())

# convert the object into a dict
playlist_tracks_dict = playlist_tracks_instance.to_dict()
# create an instance of PlaylistTracks from a dict
playlist_tracks_from_dict = PlaylistTracks.from_dict(playlist_tracks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


