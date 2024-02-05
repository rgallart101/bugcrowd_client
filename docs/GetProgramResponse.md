# GetProgramResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Program**](Program.md) |  | 
**included** | [**List[ProgramIncludedResponseInner]**](ProgramIncludedResponseInner.md) |  | [optional] 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.get_program_response import GetProgramResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetProgramResponse from a JSON string
get_program_response_instance = GetProgramResponse.from_json(json)
# print the JSON string representation of the object
print
GetProgramResponse.to_json()

# convert the object into a dict
get_program_response_dict = get_program_response_instance.to_dict()
# create an instance of GetProgramResponse from a dict
get_program_response_form_dict = get_program_response.from_dict(get_program_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


