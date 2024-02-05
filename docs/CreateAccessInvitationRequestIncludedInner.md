# CreateAccessInvitationRequestIncludedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | [**CreateAccessGrantRequestDataAttributes**](CreateAccessGrantRequestDataAttributes.md) |  | 
**relationships** | [**CreateAccessInvitationRequestIncludedInnerRelationships**](CreateAccessInvitationRequestIncludedInnerRelationships.md) |  | 

## Example

```python
from bugcrowd_client.models.create_access_invitation_request_included_inner import
    CreateAccessInvitationRequestIncludedInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccessInvitationRequestIncludedInner from a JSON string
create_access_invitation_request_included_inner_instance = CreateAccessInvitationRequestIncludedInner.from_json(json)
# print the JSON string representation of the object
print
CreateAccessInvitationRequestIncludedInner.to_json()

# convert the object into a dict
create_access_invitation_request_included_inner_dict = create_access_invitation_request_included_inner_instance.to_dict()
# create an instance of CreateAccessInvitationRequestIncludedInner from a dict
create_access_invitation_request_included_inner_form_dict = create_access_invitation_request_included_inner.from_dict(
    create_access_invitation_request_included_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


