# UpdateCustomerAssetRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | [**UpdateCustomerAssetRequestDataAttributes**](UpdateCustomerAssetRequestDataAttributes.md) |  | 
**relationships** | [**UpdateCustomerAssetRequestDataRelationships**](UpdateCustomerAssetRequestDataRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.update_customer_asset_request_data import UpdateCustomerAssetRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomerAssetRequestData from a JSON string
update_customer_asset_request_data_instance = UpdateCustomerAssetRequestData.from_json(json)
# print the JSON string representation of the object
print
UpdateCustomerAssetRequestData.to_json()

# convert the object into a dict
update_customer_asset_request_data_dict = update_customer_asset_request_data_instance.to_dict()
# create an instance of UpdateCustomerAssetRequestData from a dict
update_customer_asset_request_data_form_dict = update_customer_asset_request_data.from_dict(
    update_customer_asset_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


