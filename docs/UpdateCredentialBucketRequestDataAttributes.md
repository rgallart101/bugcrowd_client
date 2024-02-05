# UpdateCredentialBucketRequestDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**credential_type** | **str** |  | [optional] 
**credentials_per_researcher** | **int** |  | 
**description** | **str** |  | 
**is_ready** | **bool** |  | 
**low_balance_threshold** | **int** |  | [optional] 

## Example

```python
from bugcrowd_client.models.update_credential_bucket_request_data_attributes import
    UpdateCredentialBucketRequestDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCredentialBucketRequestDataAttributes from a JSON string
update_credential_bucket_request_data_attributes_instance = UpdateCredentialBucketRequestDataAttributes.from_json(json)
# print the JSON string representation of the object
print
UpdateCredentialBucketRequestDataAttributes.to_json()

# convert the object into a dict
update_credential_bucket_request_data_attributes_dict = update_credential_bucket_request_data_attributes_instance.to_dict()
# create an instance of UpdateCredentialBucketRequestDataAttributes from a dict
update_credential_bucket_request_data_attributes_form_dict = update_credential_bucket_request_data_attributes.from_dict(
    update_credential_bucket_request_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


