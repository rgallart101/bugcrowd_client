# CreateTargetGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateTargetGroupRequestData**](CreateTargetGroupRequestData.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.create_target_group_request import CreateTargetGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTargetGroupRequest from a JSON string
create_target_group_request_instance = CreateTargetGroupRequest.from_json(json)
# print the JSON string representation of the object
print
CreateTargetGroupRequest.to_json()

# convert the object into a dict
create_target_group_request_dict = create_target_group_request_instance.to_dict()
# create an instance of CreateTargetGroupRequest from a dict
create_target_group_request_form_dict = create_target_group_request.from_dict(create_target_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


