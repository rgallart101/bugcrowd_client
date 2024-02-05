# CredentialBucketAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_type** | **str** | Type of credential bucket | [optional] 
**credentials_per_researcher** | **int** | Number of credentials per researcher | [optional] 
**description** | **str** | Description of the credential bucket | [optional] 
**is_ready** | **bool** | Whether the credential bucket is ready | [optional] 
**low_balance_threshold** | **int** | Threshold at which the credential bucket is considered low on credentials | [optional] 
**name** | **str** | Name of the credential bucket | [optional] 

## Example

```python
from bugcrowd_client.models.credential_bucket_attributes import CredentialBucketAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialBucketAttributes from a JSON string
credential_bucket_attributes_instance = CredentialBucketAttributes.from_json(json)
# print the JSON string representation of the object
print
CredentialBucketAttributes.to_json()

# convert the object into a dict
credential_bucket_attributes_dict = credential_bucket_attributes_instance.to_dict()
# create an instance of CredentialBucketAttributes from a dict
credential_bucket_attributes_form_dict = credential_bucket_attributes.from_dict(credential_bucket_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


