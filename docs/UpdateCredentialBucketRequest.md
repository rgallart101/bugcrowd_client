# UpdateCredentialBucketRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UpdateCredentialBucketRequestData**](UpdateCredentialBucketRequestData.md) |  | 

## Example

```python
from bugcrowd_client.models.update_credential_bucket_request import UpdateCredentialBucketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCredentialBucketRequest from a JSON string
update_credential_bucket_request_instance = UpdateCredentialBucketRequest.from_json(json)
# print the JSON string representation of the object
print
UpdateCredentialBucketRequest.to_json()

# convert the object into a dict
update_credential_bucket_request_dict = update_credential_bucket_request_instance.to_dict()
# create an instance of UpdateCredentialBucketRequest from a dict
update_credential_bucket_request_form_dict = update_credential_bucket_request.from_dict(
    update_credential_bucket_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


