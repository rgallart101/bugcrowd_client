# CreateOrganizationRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | [**CreateOrganizationRequestDataAttributes**](CreateOrganizationRequestDataAttributes.md) |  | 

## Example

```python
from bugcrowd_client.models.create_organization_request_data import CreateOrganizationRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationRequestData from a JSON string
create_organization_request_data_instance = CreateOrganizationRequestData.from_json(json)
# print the JSON string representation of the object
print
CreateOrganizationRequestData.to_json()

# convert the object into a dict
create_organization_request_data_dict = create_organization_request_data_instance.to_dict()
# create an instance of CreateOrganizationRequestData from a dict
create_organization_request_data_form_dict = create_organization_request_data.from_dict(
    create_organization_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


