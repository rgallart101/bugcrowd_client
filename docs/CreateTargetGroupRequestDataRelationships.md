# CreateTargetGroupRequestDataRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_brief** | [**ProgramBriefNotNullable**](ProgramBriefNotNullable.md) |  | 
**reward_range** | [**RewardRangeNullable**](RewardRangeNullable.md) |  | [optional] 
**targets** | [**TargetsMax20**](TargetsMax20.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.create_target_group_request_data_relationships import
    CreateTargetGroupRequestDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTargetGroupRequestDataRelationships from a JSON string
create_target_group_request_data_relationships_instance = CreateTargetGroupRequestDataRelationships.from_json(json)
# print the JSON string representation of the object
print
CreateTargetGroupRequestDataRelationships.to_json()

# convert the object into a dict
create_target_group_request_data_relationships_dict = create_target_group_request_data_relationships_instance.to_dict()
# create an instance of CreateTargetGroupRequestDataRelationships from a dict
create_target_group_request_data_relationships_form_dict = create_target_group_request_data_relationships.from_dict(
    create_target_group_request_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


