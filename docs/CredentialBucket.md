# CredentialBucket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 
**attributes** | [**CredentialBucketAttributes**](CredentialBucketAttributes.md) |  | [optional] 
**relationships** | [**CredentialBucketRelationships**](CredentialBucketRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.credential_bucket import CredentialBucket

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialBucket from a JSON string
credential_bucket_instance = CredentialBucket.from_json(json)
# print the JSON string representation of the object
print
CredentialBucket.to_json()

# convert the object into a dict
credential_bucket_dict = credential_bucket_instance.to_dict()
# create an instance of CredentialBucket from a dict
credential_bucket_form_dict = credential_bucket.from_dict(credential_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


