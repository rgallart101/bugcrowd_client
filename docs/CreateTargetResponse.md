# CreateTargetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Target**](Target.md) |  | 

## Example

```python
from bugcrowd_client.models.create_target_response import CreateTargetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTargetResponse from a JSON string
create_target_response_instance = CreateTargetResponse.from_json(json)
# print the JSON string representation of the object
print
CreateTargetResponse.to_json()

# convert the object into a dict
create_target_response_dict = create_target_response_instance.to_dict()
# create an instance of CreateTargetResponse from a dict
create_target_response_form_dict = create_target_response.from_dict(create_target_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


