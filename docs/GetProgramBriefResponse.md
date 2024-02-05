# GetProgramBriefResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ProgramBrief**](ProgramBrief.md) |  | 
**included** | [**List[ProgramBriefIncludedResponseInner]**](ProgramBriefIncludedResponseInner.md) |  | [optional] 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.get_program_brief_response import GetProgramBriefResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetProgramBriefResponse from a JSON string
get_program_brief_response_instance = GetProgramBriefResponse.from_json(json)
# print the JSON string representation of the object
print
GetProgramBriefResponse.to_json()

# convert the object into a dict
get_program_brief_response_dict = get_program_brief_response_instance.to_dict()
# create an instance of GetProgramBriefResponse from a dict
get_program_brief_response_form_dict = get_program_brief_response.from_dict(get_program_brief_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


