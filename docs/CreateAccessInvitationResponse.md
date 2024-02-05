# CreateAccessInvitationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AccessInvitation**](AccessInvitation.md) |  | 
**included** | [**List[ResourceRole]**](ResourceRole.md) |  | 

## Example

```python
from bugcrowd_client.models.create_access_invitation_response import CreateAccessInvitationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccessInvitationResponse from a JSON string
create_access_invitation_response_instance = CreateAccessInvitationResponse.from_json(json)
# print the JSON string representation of the object
print
CreateAccessInvitationResponse.to_json()

# convert the object into a dict
create_access_invitation_response_dict = create_access_invitation_response_instance.to_dict()
# create an instance of CreateAccessInvitationResponse from a dict
create_access_invitation_response_form_dict = create_access_invitation_response.from_dict(
    create_access_invitation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


