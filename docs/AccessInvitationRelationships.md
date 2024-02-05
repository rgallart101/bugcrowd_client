# AccessInvitationRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**granting_identity** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 
**organization** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 
**resource_roles** | [**ManyRelationship**](ManyRelationship.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.access_invitation_relationships import AccessInvitationRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of AccessInvitationRelationships from a JSON string
access_invitation_relationships_instance = AccessInvitationRelationships.from_json(json)
# print the JSON string representation of the object
print
AccessInvitationRelationships.to_json()

# convert the object into a dict
access_invitation_relationships_dict = access_invitation_relationships_instance.to_dict()
# create an instance of AccessInvitationRelationships from a dict
access_invitation_relationships_form_dict = access_invitation_relationships.from_dict(
    access_invitation_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


