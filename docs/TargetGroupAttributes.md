# TargetGroupAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | URL or location of the target | [optional] 
**description** | **str** | Brief description of the target | [optional] 
**in_scope** | **bool** | Indicates whether the target is in-scope for this program | [optional] 

## Example

```python
from bugcrowd_client.models.target_group_attributes import TargetGroupAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of TargetGroupAttributes from a JSON string
target_group_attributes_instance = TargetGroupAttributes.from_json(json)
# print the JSON string representation of the object
print
TargetGroupAttributes.to_json()

# convert the object into a dict
target_group_attributes_dict = target_group_attributes_instance.to_dict()
# create an instance of TargetGroupAttributes from a dict
target_group_attributes_form_dict = target_group_attributes.from_dict(target_group_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


