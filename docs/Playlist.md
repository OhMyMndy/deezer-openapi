# Playlist


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**public** | **bool** |  | [optional] 
**is_loved_track** | **bool** |  | [optional] 
**collaborative** | **bool** |  | [optional] 
**nb_tracks** | **int** |  | [optional] 
**fans** | **int** |  | [optional] 
**link** | **str** |  | [optional] 
**share** | **str** |  | [optional] 
**picture** | **str** |  | [optional] 
**picture_small** | **str** |  | [optional] 
**picture_medium** | **str** |  | [optional] 
**picture_big** | **str** |  | [optional] 
**picture_xl** | **str** |  | [optional] 
**checksum** | **str** |  | [optional] 
**tracklist** | **str** |  | [optional] 
**creation_date** | **str** |  | [optional] 
**creator** | [**Creator**](Creator.md) |  | [optional] 
**type** | **str** |  | [optional] 
**tracks** | [**PlaylistTracks**](PlaylistTracks.md) |  | [optional] 

## Example

```python
from openapi_client.models.playlist import Playlist

# TODO update the JSON string below
json = "{}"
# create an instance of Playlist from a JSON string
playlist_instance = Playlist.from_json(json)
# print the JSON string representation of the object
print(Playlist.to_json())

# convert the object into a dict
playlist_dict = playlist_instance.to_dict()
# create an instance of Playlist from a dict
playlist_from_dict = Playlist.from_dict(playlist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


