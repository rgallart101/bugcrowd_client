# AccessInvitationAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**grantee_email** | **str** |  | [optional] 

## Example

```python
from bugcrowd_client.models.access_invitation_attributes import AccessInvitationAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AccessInvitationAttributes from a JSON string
access_invitation_attributes_instance = AccessInvitationAttributes.from_json(json)
# print the JSON string representation of the object
print
AccessInvitationAttributes.to_json()

# convert the object into a dict
access_invitation_attributes_dict = access_invitation_attributes_instance.to_dict()
# create an instance of AccessInvitationAttributes from a dict
access_invitation_attributes_form_dict = access_invitation_attributes.from_dict(access_invitation_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


