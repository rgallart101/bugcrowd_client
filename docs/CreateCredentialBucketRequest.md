# CreateCredentialBucketRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateCredentialBucketRequestData**](CreateCredentialBucketRequestData.md) |  | 

## Example

```python
from bugcrowd_client.models.create_credential_bucket_request import CreateCredentialBucketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCredentialBucketRequest from a JSON string
create_credential_bucket_request_instance = CreateCredentialBucketRequest.from_json(json)
# print the JSON string representation of the object
print
CreateCredentialBucketRequest.to_json()

# convert the object into a dict
create_credential_bucket_request_dict = create_credential_bucket_request_instance.to_dict()
# create an instance of CreateCredentialBucketRequest from a dict
create_credential_bucket_request_form_dict = create_credential_bucket_request.from_dict(
    create_credential_bucket_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


