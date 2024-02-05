# CreateTargetGroupRequestDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**in_scope** | **bool** |  | 

## Example

```python
from bugcrowd_client.models.create_target_group_request_data_attributes import CreateTargetGroupRequestDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTargetGroupRequestDataAttributes from a JSON string
create_target_group_request_data_attributes_instance = CreateTargetGroupRequestDataAttributes.from_json(json)
# print the JSON string representation of the object
print
CreateTargetGroupRequestDataAttributes.to_json()

# convert the object into a dict
create_target_group_request_data_attributes_dict = create_target_group_request_data_attributes_instance.to_dict()
# create an instance of CreateTargetGroupRequestDataAttributes from a dict
create_target_group_request_data_attributes_form_dict = create_target_group_request_data_attributes.from_dict(
    create_target_group_request_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


