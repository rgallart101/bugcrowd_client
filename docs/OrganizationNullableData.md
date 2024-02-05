# OrganizationNullableData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 

## Example

```python
from bugcrowd_client.models.organization_nullable_data import OrganizationNullableData

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationNullableData from a JSON string
organization_nullable_data_instance = OrganizationNullableData.from_json(json)
# print the JSON string representation of the object
print
OrganizationNullableData.to_json()

# convert the object into a dict
organization_nullable_data_dict = organization_nullable_data_instance.to_dict()
# create an instance of OrganizationNullableData from a dict
organization_nullable_data_form_dict = organization_nullable_data.from_dict(organization_nullable_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


