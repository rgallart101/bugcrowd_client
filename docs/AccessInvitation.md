# AccessInvitation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 
**attributes** | [**AccessInvitationAttributes**](AccessInvitationAttributes.md) |  | [optional] 
**relationships** | [**AccessInvitationRelationships**](AccessInvitationRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.access_invitation import AccessInvitation

# TODO update the JSON string below
json = "{}"
# create an instance of AccessInvitation from a JSON string
access_invitation_instance = AccessInvitation.from_json(json)
# print the JSON string representation of the object
print
AccessInvitation.to_json()

# convert the object into a dict
access_invitation_dict = access_invitation_instance.to_dict()
# create an instance of AccessInvitation from a dict
access_invitation_form_dict = access_invitation.from_dict(access_invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


