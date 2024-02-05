# ResourceRoleRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_invitation** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 
**resource** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.resource_role_relationships import ResourceRoleRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRoleRelationships from a JSON string
resource_role_relationships_instance = ResourceRoleRelationships.from_json(json)
# print the JSON string representation of the object
print
ResourceRoleRelationships.to_json()

# convert the object into a dict
resource_role_relationships_dict = resource_role_relationships_instance.to_dict()
# create an instance of ResourceRoleRelationships from a dict
resource_role_relationships_form_dict = resource_role_relationships.from_dict(resource_role_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


