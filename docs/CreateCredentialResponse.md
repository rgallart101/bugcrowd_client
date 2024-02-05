# CreateCredentialResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Credential**](Credential.md) |  | 

## Example

```python
from bugcrowd_client.models.create_credential_response import CreateCredentialResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCredentialResponse from a JSON string
create_credential_response_instance = CreateCredentialResponse.from_json(json)
# print the JSON string representation of the object
print
CreateCredentialResponse.to_json()

# convert the object into a dict
create_credential_response_dict = create_credential_response_instance.to_dict()
# create an instance of CreateCredentialResponse from a dict
create_credential_response_form_dict = create_credential_response.from_dict(create_credential_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


