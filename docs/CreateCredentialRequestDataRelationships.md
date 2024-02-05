# CreateCredentialRequestDataRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_bucket** | [**CredentialBucketNotNullable**](CredentialBucketNotNullable.md) |  | 
**user** | [**UserNotNullable**](UserNotNullable.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.create_credential_request_data_relationships import CreateCredentialRequestDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCredentialRequestDataRelationships from a JSON string
create_credential_request_data_relationships_instance = CreateCredentialRequestDataRelationships.from_json(json)
# print the JSON string representation of the object
print
CreateCredentialRequestDataRelationships.to_json()

# convert the object into a dict
create_credential_request_data_relationships_dict = create_credential_request_data_relationships_instance.to_dict()
# create an instance of CreateCredentialRequestDataRelationships from a dict
create_credential_request_data_relationships_form_dict = create_credential_request_data_relationships.from_dict(
    create_credential_request_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


