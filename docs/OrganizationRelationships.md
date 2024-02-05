# OrganizationRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**targets** | [**ManyRelationship**](ManyRelationship.md) |  | [optional] 
**programs** | [**ManyRelationship**](ManyRelationship.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.organization_relationships import OrganizationRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationRelationships from a JSON string
organization_relationships_instance = OrganizationRelationships.from_json(json)
# print the JSON string representation of the object
print
OrganizationRelationships.to_json()

# convert the object into a dict
organization_relationships_dict = organization_relationships_instance.to_dict()
# create an instance of OrganizationRelationships from a dict
organization_relationships_form_dict = organization_relationships.from_dict(organization_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


