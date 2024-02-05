# ListOrganizationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Organization]**](Organization.md) |  | 
**included** | [**List[OrganizationIncludedResponseInner]**](OrganizationIncludedResponseInner.md) |  | [optional] 
**links** | [**NavLinks**](NavLinks.md) |  | [optional] 
**meta** | [**RelationshipCountMetaData**](RelationshipCountMetaData.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.list_organizations_response import ListOrganizationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListOrganizationsResponse from a JSON string
list_organizations_response_instance = ListOrganizationsResponse.from_json(json)
# print the JSON string representation of the object
print
ListOrganizationsResponse.to_json()

# convert the object into a dict
list_organizations_response_dict = list_organizations_response_instance.to_dict()
# create an instance of ListOrganizationsResponse from a dict
list_organizations_response_form_dict = list_organizations_response.from_dict(list_organizations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


