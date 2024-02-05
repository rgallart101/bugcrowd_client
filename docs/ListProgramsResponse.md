# ListProgramsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Program]**](Program.md) |  | 
**included** | [**List[ProgramIncludedResponseInner]**](ProgramIncludedResponseInner.md) |  | [optional] 
**meta** | [**RelationshipCountMetaData**](RelationshipCountMetaData.md) |  | [optional] 
**links** | [**NavLinks**](NavLinks.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.list_programs_response import ListProgramsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListProgramsResponse from a JSON string
list_programs_response_instance = ListProgramsResponse.from_json(json)
# print the JSON string representation of the object
print
ListProgramsResponse.to_json()

# convert the object into a dict
list_programs_response_dict = list_programs_response_instance.to_dict()
# create an instance of ListProgramsResponse from a dict
list_programs_response_form_dict = list_programs_response.from_dict(list_programs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


