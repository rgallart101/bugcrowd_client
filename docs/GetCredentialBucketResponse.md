# GetCredentialBucketResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CredentialBucket**](CredentialBucket.md) |  | 
**included** | [**List[Credential]**](Credential.md) |  | [optional] 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.get_credential_bucket_response import GetCredentialBucketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCredentialBucketResponse from a JSON string
get_credential_bucket_response_instance = GetCredentialBucketResponse.from_json(json)
# print the JSON string representation of the object
print
GetCredentialBucketResponse.to_json()

# convert the object into a dict
get_credential_bucket_response_dict = get_credential_bucket_response_instance.to_dict()
# create an instance of GetCredentialBucketResponse from a dict
get_credential_bucket_response_form_dict = get_credential_bucket_response.from_dict(get_credential_bucket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


