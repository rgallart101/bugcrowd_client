# IdentityNullableData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 

## Example

```python
from bugcrowd_client.models.identity_nullable_data import IdentityNullableData

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityNullableData from a JSON string
identity_nullable_data_instance = IdentityNullableData.from_json(json)
# print the JSON string representation of the object
print
IdentityNullableData.to_json()

# convert the object into a dict
identity_nullable_data_dict = identity_nullable_data_instance.to_dict()
# create an instance of IdentityNullableData from a dict
identity_nullable_data_form_dict = identity_nullable_data.from_dict(identity_nullable_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


