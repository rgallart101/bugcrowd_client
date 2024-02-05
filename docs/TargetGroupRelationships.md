# TargetGroupRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**targets** | [**ManyRelationship**](ManyRelationship.md) |  | [optional] 
**program_brief** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 
**reward_range** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.target_group_relationships import TargetGroupRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of TargetGroupRelationships from a JSON string
target_group_relationships_instance = TargetGroupRelationships.from_json(json)
# print the JSON string representation of the object
print
TargetGroupRelationships.to_json()

# convert the object into a dict
target_group_relationships_dict = target_group_relationships_instance.to_dict()
# create an instance of TargetGroupRelationships from a dict
target_group_relationships_form_dict = target_group_relationships.from_dict(target_group_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


