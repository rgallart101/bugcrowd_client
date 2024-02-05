# UpdateCustomerAssetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UpdateCustomerAssetRequestData**](UpdateCustomerAssetRequestData.md) |  | 

## Example

```python
from bugcrowd_client.models.update_customer_asset_request import UpdateCustomerAssetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomerAssetRequest from a JSON string
update_customer_asset_request_instance = UpdateCustomerAssetRequest.from_json(json)
# print the JSON string representation of the object
print
UpdateCustomerAssetRequest.to_json()

# convert the object into a dict
update_customer_asset_request_dict = update_customer_asset_request_instance.to_dict()
# create an instance of UpdateCustomerAssetRequest from a dict
update_customer_asset_request_form_dict = update_customer_asset_request.from_dict(update_customer_asset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


