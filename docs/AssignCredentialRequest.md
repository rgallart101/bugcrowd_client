# AssignCredentialRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AssignCredentialRequestData**](AssignCredentialRequestData.md) |  | 

## Example

```python
from bugcrowd_client.models.assign_credential_request import AssignCredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignCredentialRequest from a JSON string
assign_credential_request_instance = AssignCredentialRequest.from_json(json)
# print the JSON string representation of the object
print
AssignCredentialRequest.to_json()

# convert the object into a dict
assign_credential_request_dict = assign_credential_request_instance.to_dict()
# create an instance of AssignCredentialRequest from a dict
assign_credential_request_form_dict = assign_credential_request.from_dict(assign_credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


