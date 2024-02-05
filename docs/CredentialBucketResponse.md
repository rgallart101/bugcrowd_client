# CredentialBucketResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CredentialBucket**](CredentialBucket.md) |  | 

## Example

```python
from bugcrowd_client.models.credential_bucket_response import CredentialBucketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialBucketResponse from a JSON string
credential_bucket_response_instance = CredentialBucketResponse.from_json(json)
# print the JSON string representation of the object
print
CredentialBucketResponse.to_json()

# convert the object into a dict
credential_bucket_response_dict = credential_bucket_response_instance.to_dict()
# create an instance of CredentialBucketResponse from a dict
credential_bucket_response_form_dict = credential_bucket_response.from_dict(credential_bucket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


