# CredentialBucketRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**ManyRelationship**](ManyRelationship.md) |  | [optional] 
**bounty** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.credential_bucket_relationships import CredentialBucketRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialBucketRelationships from a JSON string
credential_bucket_relationships_instance = CredentialBucketRelationships.from_json(json)
# print the JSON string representation of the object
print
CredentialBucketRelationships.to_json()

# convert the object into a dict
credential_bucket_relationships_dict = credential_bucket_relationships_instance.to_dict()
# create an instance of CredentialBucketRelationships from a dict
credential_bucket_relationships_form_dict = credential_bucket_relationships.from_dict(
    credential_bucket_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


