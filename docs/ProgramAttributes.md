# ProgramAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Unique program code, used in the URL | [optional] 
**name** | **str** | Name of the program | [optional] 

## Example

```python
from bugcrowd_client.models.program_attributes import ProgramAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramAttributes from a JSON string
program_attributes_instance = ProgramAttributes.from_json(json)
# print the JSON string representation of the object
print
ProgramAttributes.to_json()

# convert the object into a dict
program_attributes_dict = program_attributes_instance.to_dict()
# create an instance of ProgramAttributes from a dict
program_attributes_form_dict = program_attributes.from_dict(program_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


