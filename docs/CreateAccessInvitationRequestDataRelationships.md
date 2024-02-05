# CreateAccessInvitationRequestDataRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | [**CreateAccessInvitationRequestDataRelationshipsOrganization**](CreateAccessInvitationRequestDataRelationshipsOrganization.md) |  | 

## Example

```python
from bugcrowd_client.models.create_access_invitation_request_data_relationships import
    CreateAccessInvitationRequestDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccessInvitationRequestDataRelationships from a JSON string
create_access_invitation_request_data_relationships_instance = CreateAccessInvitationRequestDataRelationships.from_json(
    json)
# print the JSON string representation of the object
print
CreateAccessInvitationRequestDataRelationships.to_json()

# convert the object into a dict
create_access_invitation_request_data_relationships_dict = create_access_invitation_request_data_relationships_instance.to_dict()
# create an instance of CreateAccessInvitationRequestDataRelationships from a dict
create_access_invitation_request_data_relationships_form_dict = create_access_invitation_request_data_relationships.from_dict(
    create_access_invitation_request_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


