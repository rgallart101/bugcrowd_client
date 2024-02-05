# AssignCredentialRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | [**AssignCredentialRequestDataAttributes**](AssignCredentialRequestDataAttributes.md) |  | 

## Example

```python
from bugcrowd_client.models.assign_credential_request_data import AssignCredentialRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of AssignCredentialRequestData from a JSON string
assign_credential_request_data_instance = AssignCredentialRequestData.from_json(json)
# print the JSON string representation of the object
print
AssignCredentialRequestData.to_json()

# convert the object into a dict
assign_credential_request_data_dict = assign_credential_request_data_instance.to_dict()
# create an instance of AssignCredentialRequestData from a dict
assign_credential_request_data_form_dict = assign_credential_request_data.from_dict(assign_credential_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


