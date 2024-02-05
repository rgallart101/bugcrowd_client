# UpdateCustomerAssetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CustomerAsset**](CustomerAsset.md) |  | 

## Example

```python
from bugcrowd_client.models.update_customer_asset_response import UpdateCustomerAssetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomerAssetResponse from a JSON string
update_customer_asset_response_instance = UpdateCustomerAssetResponse.from_json(json)
# print the JSON string representation of the object
print
UpdateCustomerAssetResponse.to_json()

# convert the object into a dict
update_customer_asset_response_dict = update_customer_asset_response_instance.to_dict()
# create an instance of UpdateCustomerAssetResponse from a dict
update_customer_asset_response_form_dict = update_customer_asset_response.from_dict(update_customer_asset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


