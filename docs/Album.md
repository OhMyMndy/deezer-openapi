# Album


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**upc** | **str** |  | [optional] 
**cover** | **str** |  | [optional] 
**cover_small** | **str** |  | [optional] 
**cover_medium** | **str** |  | [optional] 
**cover_big** | **str** |  | [optional] 
**cover_xl** | **str** |  | [optional] 
**md5_image** | **str** |  | [optional] 
**tracklist** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**genre_id** | **int** |  | [optional] 
**genres** | [**Genres**](Genres.md) |  | [optional] 
**label** | **str** |  | [optional] 
**nb_tracks** | **int** |  | [optional] 
**duration** | **int** |  | [optional] 
**fans** | **int** |  | [optional] 
**release_date** | **str** |  | [optional] 
**record_type** | **str** |  | [optional] 
**available** | **bool** |  | [optional] 
**explicit_lyrics** | **bool** |  | [optional] 
**explicit_content_lyrics** | **int** |  | [optional] 
**explicit_content_cover** | **int** |  | [optional] 
**contributors** | [**List[Artist]**](Artist.md) |  | [optional] 
**artist** | [**Artist**](Artist.md) |  | [optional] 
**tracks** | [**Tracks**](Tracks.md) |  | [optional] 

## Example

```python
from openapi_client.models.album import Album

# TODO update the JSON string below
json = "{}"
# create an instance of Album from a JSON string
album_instance = Album.from_json(json)
# print the JSON string representation of the object
print(Album.to_json())

# convert the object into a dict
album_dict = album_instance.to_dict()
# create an instance of Album from a dict
album_from_dict = Album.from_dict(album_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


