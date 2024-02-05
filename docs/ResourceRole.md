# ResourceRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 
**attributes** | [**ResourceRoleAttributes**](ResourceRoleAttributes.md) |  | [optional] 
**relationships** | [**ResourceRoleRelationships**](ResourceRoleRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.resource_role import ResourceRole

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRole from a JSON string
resource_role_instance = ResourceRole.from_json(json)
# print the JSON string representation of the object
print
ResourceRole.to_json()

# convert the object into a dict
resource_role_dict = resource_role_instance.to_dict()
# create an instance of ResourceRole from a dict
resource_role_form_dict = resource_role.from_dict(resource_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


