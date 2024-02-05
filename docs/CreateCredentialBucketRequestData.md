# CreateCredentialBucketRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | [**CreateCredentialBucketRequestDataAttributes**](CreateCredentialBucketRequestDataAttributes.md) |  | 
**relationships** | [**CreateCredentialBucketRequestDataRelationships**](CreateCredentialBucketRequestDataRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.create_credential_bucket_request_data import CreateCredentialBucketRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCredentialBucketRequestData from a JSON string
create_credential_bucket_request_data_instance = CreateCredentialBucketRequestData.from_json(json)
# print the JSON string representation of the object
print
CreateCredentialBucketRequestData.to_json()

# convert the object into a dict
create_credential_bucket_request_data_dict = create_credential_bucket_request_data_instance.to_dict()
# create an instance of CreateCredentialBucketRequestData from a dict
create_credential_bucket_request_data_form_dict = create_credential_bucket_request_data.from_dict(
    create_credential_bucket_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


