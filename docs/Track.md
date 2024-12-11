# Track


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**readable** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**title_short** | **str** |  | [optional] 
**title_version** | **str** |  | [optional] 
**irsc** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**rank** | **int** |  | [optional] 
**explicit_lyrics** | **bool** |  | [optional] 
**explicit_content_lyrics** | **int** |  | [optional] 
**explicit_content_cover** | **int** |  | [optional] 
**preview** | **str** |  | [optional] 
**md5_image** | **str** |  | [optional] 
**time_add** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**artist** | [**Artist**](Artist.md) |  | [optional] 
**album** | [**Album**](Album.md) |  | [optional] 

## Example

```python
from openapi_client.models.track import Track

# TODO update the JSON string below
json = "{}"
# create an instance of Track from a JSON string
track_instance = Track.from_json(json)
# print the JSON string representation of the object
print(Track.to_json())

# convert the object into a dict
track_dict = track_instance.to_dict()
# create an instance of Track from a dict
track_from_dict = Track.from_dict(track_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


