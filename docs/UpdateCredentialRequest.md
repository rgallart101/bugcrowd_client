# UpdateCredentialRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UpdateCredentialRequestData**](UpdateCredentialRequestData.md) |  | 

## Example

```python
from bugcrowd_client.models.update_credential_request import UpdateCredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCredentialRequest from a JSON string
update_credential_request_instance = UpdateCredentialRequest.from_json(json)
# print the JSON string representation of the object
print
UpdateCredentialRequest.to_json()

# convert the object into a dict
update_credential_request_dict = update_credential_request_instance.to_dict()
# create an instance of UpdateCredentialRequest from a dict
update_credential_request_form_dict = update_credential_request.from_dict(update_credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


