# CreateTargetGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TargetGroup**](TargetGroup.md) |  | 

## Example

```python
from bugcrowd_client.models.create_target_group_response import CreateTargetGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTargetGroupResponse from a JSON string
create_target_group_response_instance = CreateTargetGroupResponse.from_json(json)
# print the JSON string representation of the object
print
CreateTargetGroupResponse.to_json()

# convert the object into a dict
create_target_group_response_dict = create_target_group_response_instance.to_dict()
# create an instance of CreateTargetGroupResponse from a dict
create_target_group_response_form_dict = create_target_group_response.from_dict(create_target_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


