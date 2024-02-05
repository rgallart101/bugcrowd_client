# AccessInvitationIncludedResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | 
**attributes** | [**ResourceRoleAttributes**](ResourceRoleAttributes.md) |  | [optional] 
**relationships** | [**ResourceRoleRelationships**](ResourceRoleRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.access_invitation_included_response_inner import AccessInvitationIncludedResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccessInvitationIncludedResponseInner from a JSON string
access_invitation_included_response_inner_instance = AccessInvitationIncludedResponseInner.from_json(json)
# print the JSON string representation of the object
print
AccessInvitationIncludedResponseInner.to_json()

# convert the object into a dict
access_invitation_included_response_inner_dict = access_invitation_included_response_inner_instance.to_dict()
# create an instance of AccessInvitationIncludedResponseInner from a dict
access_invitation_included_response_inner_form_dict = access_invitation_included_response_inner.from_dict(
    access_invitation_included_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


