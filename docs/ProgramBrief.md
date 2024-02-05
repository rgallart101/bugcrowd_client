# ProgramBrief


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 
**attributes** | [**ProgramBriefAttributes**](ProgramBriefAttributes.md) |  | [optional] 
**relationships** | [**ProgramBriefRelationships**](ProgramBriefRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.program_brief import ProgramBrief

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramBrief from a JSON string
program_brief_instance = ProgramBrief.from_json(json)
# print the JSON string representation of the object
print
ProgramBrief.to_json()

# convert the object into a dict
program_brief_dict = program_brief_instance.to_dict()
# create an instance of ProgramBrief from a dict
program_brief_form_dict = program_brief.from_dict(program_brief_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


