# TargetGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 
**attributes** | [**TargetGroupAttributes**](TargetGroupAttributes.md) |  | [optional] 
**relationships** | [**TargetGroupRelationships**](TargetGroupRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.target_group import TargetGroup

# TODO update the JSON string below
json = "{}"
# create an instance of TargetGroup from a JSON string
target_group_instance = TargetGroup.from_json(json)
# print the JSON string representation of the object
print
TargetGroup.to_json()

# convert the object into a dict
target_group_dict = target_group_instance.to_dict()
# create an instance of TargetGroup from a dict
target_group_form_dict = target_group.from_dict(target_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


