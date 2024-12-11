# Artist


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**picture** | **str** |  | [optional] 
**picture_small** | **str** |  | [optional] 
**picture_medium** | **str** |  | [optional] 
**picture_big** | **str** |  | [optional] 
**picture_xl** | **str** |  | [optional] 
**tracklist** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**artist** | [**Artist**](Artist.md) |  | [optional] 

## Example

```python
from openapi_client.models.artist import Artist

# TODO update the JSON string below
json = "{}"
# create an instance of Artist from a JSON string
artist_instance = Artist.from_json(json)
# print the JSON string representation of the object
print(Artist.to_json())

# convert the object into a dict
artist_dict = artist_instance.to_dict()
# create an instance of Artist from a dict
artist_from_dict = Artist.from_dict(artist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


