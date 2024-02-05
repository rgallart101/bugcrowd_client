# CreateAccessGrantRequestDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**OrganizationOrProgramRolesEnum**](OrganizationOrProgramRolesEnum.md) |  | 

## Example

```python
from bugcrowd_client.models.create_access_grant_request_data_attributes import CreateAccessGrantRequestDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccessGrantRequestDataAttributes from a JSON string
create_access_grant_request_data_attributes_instance = CreateAccessGrantRequestDataAttributes.from_json(json)
# print the JSON string representation of the object
print
CreateAccessGrantRequestDataAttributes.to_json()

# convert the object into a dict
create_access_grant_request_data_attributes_dict = create_access_grant_request_data_attributes_instance.to_dict()
# create an instance of CreateAccessGrantRequestDataAttributes from a dict
create_access_grant_request_data_attributes_form_dict = create_access_grant_request_data_attributes.from_dict(
    create_access_grant_request_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


