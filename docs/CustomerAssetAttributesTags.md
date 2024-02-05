# CustomerAssetAttributesTags

An object which describes the tags associated with the asset. The categories are  `cve`- A list of Common Vulnerabilities and Exposures tags.  `cpe`- A Common Platform Enumeration tag which abides by the standard of the CPE Version.  `additional`- A list of additional tags which help in describing the asset. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpe** | **str** | A Common Platform Enumeration tag. The CPE needs to abide by the standard of the CPE Version 2.3 was released by the U.S. National Institute of Standards and Technology (NIST) in August 2011.  Schema for this &#x60;cpe:&lt;cpe_version&gt;:&lt;part&gt;:&lt;vendor&gt;:&lt;product&gt;:&lt;version&gt;:&lt;update&gt;:&lt;edition&gt;:&lt;language&gt;:&lt;sw_edition&gt;:&lt;target_sw&gt;:&lt;target_hw&gt;:&lt;other&gt;&#x60;  | [optional] 
**cve** | **List[str]** | Indicates a list of Common Vulnerabilities and Exposures tags.  These are usually CVE IDs and can have four (4) or more digits in the sequence number portion of the ID.  For example, CVE-YYYY-NNNN with 4 digits in the sequence number, CVE-YYYY-NNNNN with 5 digits in the sequence number, CVE-YYYY-NNNNNNN with 7 digits in the sequence number, and so on.  | [optional] 
**additional** | **List[str]** | A list of additional tags or user defined custom tags which help in describing the asset. | [optional] 

## Example

```python
from bugcrowd_client.models.customer_asset_attributes_tags import CustomerAssetAttributesTags

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerAssetAttributesTags from a JSON string
customer_asset_attributes_tags_instance = CustomerAssetAttributesTags.from_json(json)
# print the JSON string representation of the object
print
CustomerAssetAttributesTags.to_json()

# convert the object into a dict
customer_asset_attributes_tags_dict = customer_asset_attributes_tags_instance.to_dict()
# create an instance of CustomerAssetAttributesTags from a dict
customer_asset_attributes_tags_form_dict = customer_asset_attributes_tags.from_dict(customer_asset_attributes_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


