# CreateOrganizationRequestDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from bugcrowd_client.models.create_organization_request_data_attributes import CreateOrganizationRequestDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationRequestDataAttributes from a JSON string
create_organization_request_data_attributes_instance = CreateOrganizationRequestDataAttributes.from_json(json)
# print the JSON string representation of the object
print
CreateOrganizationRequestDataAttributes.to_json()

# convert the object into a dict
create_organization_request_data_attributes_dict = create_organization_request_data_attributes_instance.to_dict()
# create an instance of CreateOrganizationRequestDataAttributes from a dict
create_organization_request_data_attributes_form_dict = create_organization_request_data_attributes.from_dict(
    create_organization_request_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


