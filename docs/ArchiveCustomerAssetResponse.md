# ArchiveCustomerAssetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArchiveCustomerAssetResponseData**](ArchiveCustomerAssetResponseData.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.archive_customer_asset_response import ArchiveCustomerAssetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArchiveCustomerAssetResponse from a JSON string
archive_customer_asset_response_instance = ArchiveCustomerAssetResponse.from_json(json)
# print the JSON string representation of the object
print
ArchiveCustomerAssetResponse.to_json()

# convert the object into a dict
archive_customer_asset_response_dict = archive_customer_asset_response_instance.to_dict()
# create an instance of ArchiveCustomerAssetResponse from a dict
archive_customer_asset_response_form_dict = archive_customer_asset_response.from_dict(
    archive_customer_asset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


