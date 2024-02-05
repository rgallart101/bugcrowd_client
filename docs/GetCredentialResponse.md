# GetCredentialResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Credential**](Credential.md) |  | 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.get_credential_response import GetCredentialResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCredentialResponse from a JSON string
get_credential_response_instance = GetCredentialResponse.from_json(json)
# print the JSON string representation of the object
print
GetCredentialResponse.to_json()

# convert the object into a dict
get_credential_response_dict = get_credential_response_instance.to_dict()
# create an instance of GetCredentialResponse from a dict
get_credential_response_form_dict = get_credential_response.from_dict(get_credential_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


