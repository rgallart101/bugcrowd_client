# CreateAccessGrantRequestDataRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grantee** | [**IdentityNotNullable**](IdentityNotNullable.md) |  | 
**resource** | [**CreateAccessGrantRequestDataRelationshipsResource**](CreateAccessGrantRequestDataRelationshipsResource.md) |  | 

## Example

```python
from bugcrowd_client.models.create_access_grant_request_data_relationships import
    CreateAccessGrantRequestDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccessGrantRequestDataRelationships from a JSON string
create_access_grant_request_data_relationships_instance = CreateAccessGrantRequestDataRelationships.from_json(json)
# print the JSON string representation of the object
print
CreateAccessGrantRequestDataRelationships.to_json()

# convert the object into a dict
create_access_grant_request_data_relationships_dict = create_access_grant_request_data_relationships_instance.to_dict()
# create an instance of CreateAccessGrantRequestDataRelationships from a dict
create_access_grant_request_data_relationships_form_dict = create_access_grant_request_data_relationships.from_dict(
    create_access_grant_request_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


