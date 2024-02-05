# CreateCredentialRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateCredentialRequestData**](CreateCredentialRequestData.md) |  | 

## Example

```python
from bugcrowd_client.models.create_credential_request import CreateCredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCredentialRequest from a JSON string
create_credential_request_instance = CreateCredentialRequest.from_json(json)
# print the JSON string representation of the object
print
CreateCredentialRequest.to_json()

# convert the object into a dict
create_credential_request_dict = create_credential_request_instance.to_dict()
# create an instance of CreateCredentialRequest from a dict
create_credential_request_form_dict = create_credential_request.from_dict(create_credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


