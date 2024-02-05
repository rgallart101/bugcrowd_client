# ProgramRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_brief** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 
**organization** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 
**submissions** | [**ManyRelationship**](ManyRelationship.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.program_relationships import ProgramRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramRelationships from a JSON string
program_relationships_instance = ProgramRelationships.from_json(json)
# print the JSON string representation of the object
print
ProgramRelationships.to_json()

# convert the object into a dict
program_relationships_dict = program_relationships_instance.to_dict()
# create an instance of ProgramRelationships from a dict
program_relationships_form_dict = program_relationships.from_dict(program_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


