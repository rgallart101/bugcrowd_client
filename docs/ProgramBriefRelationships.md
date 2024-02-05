# ProgramBriefRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 
**target_groups** | [**ManyRelationship**](ManyRelationship.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.program_brief_relationships import ProgramBriefRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramBriefRelationships from a JSON string
program_brief_relationships_instance = ProgramBriefRelationships.from_json(json)
# print the JSON string representation of the object
print
ProgramBriefRelationships.to_json()

# convert the object into a dict
program_brief_relationships_dict = program_brief_relationships_instance.to_dict()
# create an instance of ProgramBriefRelationships from a dict
program_brief_relationships_form_dict = program_brief_relationships.from_dict(program_brief_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


