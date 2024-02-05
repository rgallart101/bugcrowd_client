# TargetRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**submissions** | [**ManyRelationship**](ManyRelationship.md) |  | [optional] 
**organization** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.target_relationships import TargetRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of TargetRelationships from a JSON string
target_relationships_instance = TargetRelationships.from_json(json)
# print the JSON string representation of the object
print
TargetRelationships.to_json()

# convert the object into a dict
target_relationships_dict = target_relationships_instance.to_dict()
# create an instance of TargetRelationships from a dict
target_relationships_form_dict = target_relationships.from_dict(target_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


