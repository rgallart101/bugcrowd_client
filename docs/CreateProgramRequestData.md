# CreateProgramRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | [**CreateProgramRequestDataAttributes**](CreateProgramRequestDataAttributes.md) |  | 
**relationships** | [**CreateCustomerAssetRequestDataRelationships**](CreateCustomerAssetRequestDataRelationships.md) |  | 

## Example

```python
from bugcrowd_client.models.create_program_request_data import CreateProgramRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProgramRequestData from a JSON string
create_program_request_data_instance = CreateProgramRequestData.from_json(json)
# print the JSON string representation of the object
print
CreateProgramRequestData.to_json()

# convert the object into a dict
create_program_request_data_dict = create_program_request_data_instance.to_dict()
# create an instance of CreateProgramRequestData from a dict
create_program_request_data_form_dict = create_program_request_data.from_dict(create_program_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


