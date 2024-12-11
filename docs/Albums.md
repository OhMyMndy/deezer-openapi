# Albums


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Album]**](Album.md) |  | [optional] 

## Example

```python
from openapi_client.models.albums import Albums

# TODO update the JSON string below
json = "{}"
# create an instance of Albums from a JSON string
albums_instance = Albums.from_json(json)
# print the JSON string representation of the object
print(Albums.to_json())

# convert the object into a dict
albums_dict = albums_instance.to_dict()
# create an instance of Albums from a dict
albums_from_dict = Albums.from_dict(albums_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


