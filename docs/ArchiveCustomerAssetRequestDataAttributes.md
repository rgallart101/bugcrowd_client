# ArchiveCustomerAssetRequestDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Specifies a reason for archiving the asset. | 
**comment** | **str** | A brief comment describing why the asset is being archived. | [optional] 

## Example

```python
from bugcrowd_client.models.archive_customer_asset_request_data_attributes import
    ArchiveCustomerAssetRequestDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ArchiveCustomerAssetRequestDataAttributes from a JSON string
archive_customer_asset_request_data_attributes_instance = ArchiveCustomerAssetRequestDataAttributes.from_json(json)
# print the JSON string representation of the object
print
ArchiveCustomerAssetRequestDataAttributes.to_json()

# convert the object into a dict
archive_customer_asset_request_data_attributes_dict = archive_customer_asset_request_data_attributes_instance.to_dict()
# create an instance of ArchiveCustomerAssetRequestDataAttributes from a dict
archive_customer_asset_request_data_attributes_form_dict = archive_customer_asset_request_data_attributes.from_dict(
    archive_customer_asset_request_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


