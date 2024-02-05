# UpdateCredentialResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Credential**](Credential.md) |  | 

## Example

```python
from bugcrowd_client.models.update_credential_response import UpdateCredentialResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCredentialResponse from a JSON string
update_credential_response_instance = UpdateCredentialResponse.from_json(json)
# print the JSON string representation of the object
print
UpdateCredentialResponse.to_json()

# convert the object into a dict
update_credential_response_dict = update_credential_response_instance.to_dict()
# create an instance of UpdateCredentialResponse from a dict
update_credential_response_form_dict = update_credential_response.from_dict(update_credential_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


