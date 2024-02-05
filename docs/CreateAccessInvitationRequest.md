# CreateAccessInvitationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateAccessInvitationRequestData**](CreateAccessInvitationRequestData.md) |  | 
**included** | [**List[CreateAccessInvitationRequestIncludedInner]**](CreateAccessInvitationRequestIncludedInner.md) |  | 

## Example

```python
from bugcrowd_client.models.create_access_invitation_request import CreateAccessInvitationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccessInvitationRequest from a JSON string
create_access_invitation_request_instance = CreateAccessInvitationRequest.from_json(json)
# print the JSON string representation of the object
print
CreateAccessInvitationRequest.to_json()

# convert the object into a dict
create_access_invitation_request_dict = create_access_invitation_request_instance.to_dict()
# create an instance of CreateAccessInvitationRequest from a dict
create_access_invitation_request_form_dict = create_access_invitation_request.from_dict(
    create_access_invitation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


