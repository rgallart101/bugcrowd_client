# OrganizationAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the organization | [optional] 

## Example

```python
from bugcrowd_client.models.organization_attributes import OrganizationAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationAttributes from a JSON string
organization_attributes_instance = OrganizationAttributes.from_json(json)
# print the JSON string representation of the object
print
OrganizationAttributes.to_json()

# convert the object into a dict
organization_attributes_dict = organization_attributes_instance.to_dict()
# create an instance of OrganizationAttributes from a dict
organization_attributes_form_dict = organization_attributes.from_dict(organization_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


