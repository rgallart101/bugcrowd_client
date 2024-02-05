# CreateAccessGrantRequestDataRelationshipsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateAccessGrantRequestDataRelationshipsResourceData**](CreateAccessGrantRequestDataRelationshipsResourceData.md) |  | 

## Example

```python
from bugcrowd_client.models.create_access_grant_request_data_relationships_resource import
    CreateAccessGrantRequestDataRelationshipsResource

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccessGrantRequestDataRelationshipsResource from a JSON string
create_access_grant_request_data_relationships_resource_instance = CreateAccessGrantRequestDataRelationshipsResource.from_json(
    json)
# print the JSON string representation of the object
print
CreateAccessGrantRequestDataRelationshipsResource.to_json()

# convert the object into a dict
create_access_grant_request_data_relationships_resource_dict = create_access_grant_request_data_relationships_resource_instance.to_dict()
# create an instance of CreateAccessGrantRequestDataRelationshipsResource from a dict
create_access_grant_request_data_relationships_resource_form_dict = create_access_grant_request_data_relationships_resource.from_dict(
    create_access_grant_request_data_relationships_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


