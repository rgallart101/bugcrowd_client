# CreateAccessInvitationRequestDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grantee_email** | **str** |  | 

## Example

```python
from bugcrowd_client.models.create_access_invitation_request_data_attributes import
    CreateAccessInvitationRequestDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccessInvitationRequestDataAttributes from a JSON string
create_access_invitation_request_data_attributes_instance = CreateAccessInvitationRequestDataAttributes.from_json(json)
# print the JSON string representation of the object
print
CreateAccessInvitationRequestDataAttributes.to_json()

# convert the object into a dict
create_access_invitation_request_data_attributes_dict = create_access_invitation_request_data_attributes_instance.to_dict()
# create an instance of CreateAccessInvitationRequestDataAttributes from a dict
create_access_invitation_request_data_attributes_form_dict = create_access_invitation_request_data_attributes.from_dict(
    create_access_invitation_request_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


