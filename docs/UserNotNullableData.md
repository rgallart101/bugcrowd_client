# UserNotNullableData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 

## Example

```python
from bugcrowd_client.models.user_not_nullable_data import UserNotNullableData

# TODO update the JSON string below
json = "{}"
# create an instance of UserNotNullableData from a JSON string
user_not_nullable_data_instance = UserNotNullableData.from_json(json)
# print the JSON string representation of the object
print
UserNotNullableData.to_json()

# convert the object into a dict
user_not_nullable_data_dict = user_not_nullable_data_instance.to_dict()
# create an instance of UserNotNullableData from a dict
user_not_nullable_data_form_dict = user_not_nullable_data.from_dict(user_not_nullable_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


