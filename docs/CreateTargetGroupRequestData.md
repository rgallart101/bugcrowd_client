# CreateTargetGroupRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | [**CreateTargetGroupRequestDataAttributes**](CreateTargetGroupRequestDataAttributes.md) |  | 
**relationships** | [**CreateTargetGroupRequestDataRelationships**](CreateTargetGroupRequestDataRelationships.md) |  | 

## Example

```python
from bugcrowd_client.models.create_target_group_request_data import CreateTargetGroupRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTargetGroupRequestData from a JSON string
create_target_group_request_data_instance = CreateTargetGroupRequestData.from_json(json)
# print the JSON string representation of the object
print
CreateTargetGroupRequestData.to_json()

# convert the object into a dict
create_target_group_request_data_dict = create_target_group_request_data_instance.to_dict()
# create an instance of CreateTargetGroupRequestData from a dict
create_target_group_request_data_form_dict = create_target_group_request_data.from_dict(
    create_target_group_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


