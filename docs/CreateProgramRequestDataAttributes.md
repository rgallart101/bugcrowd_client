# CreateProgramRequestDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**code** | **str** |  | 

## Example

```python
from bugcrowd_client.models.create_program_request_data_attributes import CreateProgramRequestDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProgramRequestDataAttributes from a JSON string
create_program_request_data_attributes_instance = CreateProgramRequestDataAttributes.from_json(json)
# print the JSON string representation of the object
print
CreateProgramRequestDataAttributes.to_json()

# convert the object into a dict
create_program_request_data_attributes_dict = create_program_request_data_attributes_instance.to_dict()
# create an instance of CreateProgramRequestDataAttributes from a dict
create_program_request_data_attributes_form_dict = create_program_request_data_attributes.from_dict(
    create_program_request_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


