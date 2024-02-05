# ArchiveCustomerAssetRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | [**ArchiveCustomerAssetRequestDataAttributes**](ArchiveCustomerAssetRequestDataAttributes.md) |  | 
**relationships** | [**UpdateCustomerAssetRequestDataRelationships**](UpdateCustomerAssetRequestDataRelationships.md) |  | 

## Example

```python
from bugcrowd_client.models.archive_customer_asset_request_data import ArchiveCustomerAssetRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ArchiveCustomerAssetRequestData from a JSON string
archive_customer_asset_request_data_instance = ArchiveCustomerAssetRequestData.from_json(json)
# print the JSON string representation of the object
print
ArchiveCustomerAssetRequestData.to_json()

# convert the object into a dict
archive_customer_asset_request_data_dict = archive_customer_asset_request_data_instance.to_dict()
# create an instance of ArchiveCustomerAssetRequestData from a dict
archive_customer_asset_request_data_form_dict = archive_customer_asset_request_data.from_dict(
    archive_customer_asset_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


