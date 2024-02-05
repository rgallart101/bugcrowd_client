# ArchiveCustomerAssetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArchiveCustomerAssetRequestData**](ArchiveCustomerAssetRequestData.md) |  | 

## Example

```python
from bugcrowd_client.models.archive_customer_asset_request import ArchiveCustomerAssetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ArchiveCustomerAssetRequest from a JSON string
archive_customer_asset_request_instance = ArchiveCustomerAssetRequest.from_json(json)
# print the JSON string representation of the object
print
ArchiveCustomerAssetRequest.to_json()

# convert the object into a dict
archive_customer_asset_request_dict = archive_customer_asset_request_instance.to_dict()
# create an instance of ArchiveCustomerAssetRequest from a dict
archive_customer_asset_request_form_dict = archive_customer_asset_request.from_dict(archive_customer_asset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


