# ResourceRoleAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**OrganizationOrProgramRolesEnum**](OrganizationOrProgramRolesEnum.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.resource_role_attributes import ResourceRoleAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRoleAttributes from a JSON string
resource_role_attributes_instance = ResourceRoleAttributes.from_json(json)
# print the JSON string representation of the object
print
ResourceRoleAttributes.to_json()

# convert the object into a dict
resource_role_attributes_dict = resource_role_attributes_instance.to_dict()
# create an instance of ResourceRoleAttributes from a dict
resource_role_attributes_form_dict = resource_role_attributes.from_dict(resource_role_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


