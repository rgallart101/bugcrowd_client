# ListCredentialBucketResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CredentialBucket]**](CredentialBucket.md) |  | 
**included** | [**List[Credential]**](Credential.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.list_credential_bucket_response import ListCredentialBucketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListCredentialBucketResponse from a JSON string
list_credential_bucket_response_instance = ListCredentialBucketResponse.from_json(json)
# print the JSON string representation of the object
print
ListCredentialBucketResponse.to_json()

# convert the object into a dict
list_credential_bucket_response_dict = list_credential_bucket_response_instance.to_dict()
# create an instance of ListCredentialBucketResponse from a dict
list_credential_bucket_response_form_dict = list_credential_bucket_response.from_dict(
    list_credential_bucket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


