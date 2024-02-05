# CreateCustomerAssetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateCustomerAssetRequestData**](CreateCustomerAssetRequestData.md) |  | 

## Example

```python
from bugcrowd_client.models.create_customer_asset_request import CreateCustomerAssetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomerAssetRequest from a JSON string
create_customer_asset_request_instance = CreateCustomerAssetRequest.from_json(json)
# print the JSON string representation of the object
print
CreateCustomerAssetRequest.to_json()

# convert the object into a dict
create_customer_asset_request_dict = create_customer_asset_request_instance.to_dict()
# create an instance of CreateCustomerAssetRequest from a dict
create_customer_asset_request_form_dict = create_customer_asset_request.from_dict(create_customer_asset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


