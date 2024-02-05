# CreateProgramRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateProgramRequestData**](CreateProgramRequestData.md) |  | 

## Example

```python
from bugcrowd_client.models.create_program_request import CreateProgramRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProgramRequest from a JSON string
create_program_request_instance = CreateProgramRequest.from_json(json)
# print the JSON string representation of the object
print
CreateProgramRequest.to_json()

# convert the object into a dict
create_program_request_dict = create_program_request_instance.to_dict()
# create an instance of CreateProgramRequest from a dict
create_program_request_form_dict = create_program_request.from_dict(create_program_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


