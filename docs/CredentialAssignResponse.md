# CredentialAssignResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Credential**](Credential.md) |  | 

## Example

```python
from bugcrowd_client.models.credential_assign_response import CredentialAssignResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialAssignResponse from a JSON string
credential_assign_response_instance = CredentialAssignResponse.from_json(json)
# print the JSON string representation of the object
print
CredentialAssignResponse.to_json()

# convert the object into a dict
credential_assign_response_dict = credential_assign_response_instance.to_dict()
# create an instance of CredentialAssignResponse from a dict
credential_assign_response_form_dict = credential_assign_response.from_dict(credential_assign_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


