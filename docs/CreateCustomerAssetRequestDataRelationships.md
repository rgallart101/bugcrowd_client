# CreateCustomerAssetRequestDataRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | [**OrganizationNotNullable**](OrganizationNotNullable.md) |  | 

## Example

```python
from bugcrowd_client.models.create_customer_asset_request_data_relationships import
    CreateCustomerAssetRequestDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomerAssetRequestDataRelationships from a JSON string
create_customer_asset_request_data_relationships_instance = CreateCustomerAssetRequestDataRelationships.from_json(json)
# print the JSON string representation of the object
print
CreateCustomerAssetRequestDataRelationships.to_json()

# convert the object into a dict
create_customer_asset_request_data_relationships_dict = create_customer_asset_request_data_relationships_instance.to_dict()
# create an instance of CreateCustomerAssetRequestDataRelationships from a dict
create_customer_asset_request_data_relationships_form_dict = create_customer_asset_request_data_relationships.from_dict(
    create_customer_asset_request_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


