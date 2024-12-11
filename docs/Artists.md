# Artists


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Artist]**](Artist.md) |  | [optional] 

## Example

```python
from openapi_client.models.artists import Artists

# TODO update the JSON string below
json = "{}"
# create an instance of Artists from a JSON string
artists_instance = Artists.from_json(json)
# print the JSON string representation of the object
print(Artists.to_json())

# convert the object into a dict
artists_dict = artists_instance.to_dict()
# create an instance of Artists from a dict
artists_from_dict = Artists.from_dict(artists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


