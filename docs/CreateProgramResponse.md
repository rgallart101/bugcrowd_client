# CreateProgramResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Program**](Program.md) |  | 

## Example

```python
from bugcrowd_client.models.create_program_response import CreateProgramResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProgramResponse from a JSON string
create_program_response_instance = CreateProgramResponse.from_json(json)
# print the JSON string representation of the object
print
CreateProgramResponse.to_json()

# convert the object into a dict
create_program_response_dict = create_program_response_instance.to_dict()
# create an instance of CreateProgramResponse from a dict
create_program_response_form_dict = create_program_response.from_dict(create_program_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


