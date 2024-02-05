# UpdateCustomerAssetRequestDataAttributesTags

To hold an object that contains tags of various categories. Commonly provided tag categories are `cve`, `cpe` or `additional` tags.  `cpe`- A Common Platform Enumeration tag which abides by the standard of the CPE Version and is a single long string. Schema for `cpe` tag - `cpe:<cpe_version>:<part>:<vendor>:<product>:<version>:<update>:<edition>:<language>:<sw_edition>:<target_sw>:<target_hw>:<other>`  `cve`- A list of Common Vulnerabilities and Exposures tags. They are often CVE IDs that can have four (4) or more digits in the sequence number portion of the ID. For example, CVE-YYYY-NNNN with 4 digits in the sequence number, CVE-YYYY-NNNNN with 5 digits in the sequence number, CVE-YYYY-NNNNNNN with 7 digits in the sequence number, and so on.  `additional`- A list of additional tags which help in describing the asset and can have any used defined string as a tag value.  Update will replace the entire list of previously added tags with list specified here. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpe** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**additional** | **List[str]** |  | [optional] 

## Example

```python
from bugcrowd_client.models.update_customer_asset_request_data_attributes_tags import
    UpdateCustomerAssetRequestDataAttributesTags

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomerAssetRequestDataAttributesTags from a JSON string
update_customer_asset_request_data_attributes_tags_instance = UpdateCustomerAssetRequestDataAttributesTags.from_json(
    json)
# print the JSON string representation of the object
print
UpdateCustomerAssetRequestDataAttributesTags.to_json()

# convert the object into a dict
update_customer_asset_request_data_attributes_tags_dict = update_customer_asset_request_data_attributes_tags_instance.to_dict()
# create an instance of UpdateCustomerAssetRequestDataAttributesTags from a dict
update_customer_asset_request_data_attributes_tags_form_dict = update_customer_asset_request_data_attributes_tags.from_dict(
    update_customer_asset_request_data_attributes_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


