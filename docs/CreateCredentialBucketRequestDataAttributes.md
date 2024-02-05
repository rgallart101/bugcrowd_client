# CreateCredentialBucketRequestDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**credential_type** | **str** |  | 
**credentials_per_researcher** | **int** |  | 
**description** | **str** |  | 
**is_ready** | **bool** |  | 
**low_balance_threshold** | **int** |  | [optional] 

## Example

```python
from bugcrowd_client.models.create_credential_bucket_request_data_attributes import
    CreateCredentialBucketRequestDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCredentialBucketRequestDataAttributes from a JSON string
create_credential_bucket_request_data_attributes_instance = CreateCredentialBucketRequestDataAttributes.from_json(json)
# print the JSON string representation of the object
print
CreateCredentialBucketRequestDataAttributes.to_json()

# convert the object into a dict
create_credential_bucket_request_data_attributes_dict = create_credential_bucket_request_data_attributes_instance.to_dict()
# create an instance of CreateCredentialBucketRequestDataAttributes from a dict
create_credential_bucket_request_data_attributes_form_dict = create_credential_bucket_request_data_attributes.from_dict(
    create_credential_bucket_request_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


