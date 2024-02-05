# CreateCustomerAssetRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | [**CreateCustomerAssetRequestDataAttributes**](CreateCustomerAssetRequestDataAttributes.md) |  | 
**relationships** | [**CreateCustomerAssetRequestDataRelationships**](CreateCustomerAssetRequestDataRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.create_customer_asset_request_data import CreateCustomerAssetRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomerAssetRequestData from a JSON string
create_customer_asset_request_data_instance = CreateCustomerAssetRequestData.from_json(json)
# print the JSON string representation of the object
print
CreateCustomerAssetRequestData.to_json()

# convert the object into a dict
create_customer_asset_request_data_dict = create_customer_asset_request_data_instance.to_dict()
# create an instance of CreateCustomerAssetRequestData from a dict
create_customer_asset_request_data_form_dict = create_customer_asset_request_data.from_dict(
    create_customer_asset_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


