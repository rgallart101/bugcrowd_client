# CreateCustomerAssetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CustomerAsset**](CustomerAsset.md) |  | 

## Example

```python
from bugcrowd_client.models.create_customer_asset_response import CreateCustomerAssetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomerAssetResponse from a JSON string
create_customer_asset_response_instance = CreateCustomerAssetResponse.from_json(json)
# print the JSON string representation of the object
print
CreateCustomerAssetResponse.to_json()

# convert the object into a dict
create_customer_asset_response_dict = create_customer_asset_response_instance.to_dict()
# create an instance of CreateCustomerAssetResponse from a dict
create_customer_asset_response_form_dict = create_customer_asset_response.from_dict(create_customer_asset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


