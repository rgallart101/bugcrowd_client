# CustomerAssetAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the asset | [optional] 
**type** | **str** | Basic categorization of the asset. The values might include &#x60;host, domain, url, android_play_store, android_apk, hardware, source_code, ios_app_store, ios_ipa, ios_test_flight, executable, cidr, fqdn, ip, api and other_asset_type&#x60;  | [optional] 
**description** | **str** | A brief description about the asset. | [optional] 
**host_name** | **str** | Host name if any for the asset. | [optional] 
**port_list** | **List[int]** | A list of port numbers for the asset between the range of 1 to 65535. | [optional] 
**ip_address** | **List[str]** | A list of IPv4 / IPv6 / CIDR range of IP Address for the asset. | [optional] 
**attributes** | [**List[CustomerAssetAttributesAttributesInner]**](CustomerAssetAttributesAttributesInner.md) | A list of key value pairs describing the attributes of the asset. One can add up to 100 attributes for each asset.  Commonly expected attributes are &#x60;external_id, external_link, record_type, autonomous_system_number etc&#x60;.  If the key is &#x60;record_type&#x60;, then its value should be in &#x60;A, AAAA, PTR, CNAME, MX, TXT, NS, SOA and SRV&#x60;.  If the key is &#x60;autonomous_system_number&#x60;, then it should be a unique 16 bit numbers between 1 and 65534 or 32 bit numbers between 131072 and 4294967294. The number should be prefixed with AS. Example - AS(number)  External ID is often a Configuration Item ID from a CMDB. Sometimes this is an ID from an external discovery scanner tool.  External link is a hyperlink or an identifier.  Customers can also specify their own attributes other than the given above list.  | [optional] 
**approved** | **bool** | Indicates if the asset is approved and ready to be used. | [optional] 
**created_at** | **datetime** | Timestamp indicating when the asset was added. | [optional] 
**source** | [**CustomerAssetSourceEnum**](CustomerAssetSourceEnum.md) |  | [optional] 
**tags** | [**CustomerAssetAttributesTags**](CustomerAssetAttributesTags.md) |  | [optional] 
**last_modified_at** | **datetime** | Timestamp indicating when the asset was last modified. | [optional] 

## Example

```python
from bugcrowd_client.models.customer_asset_attributes import CustomerAssetAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerAssetAttributes from a JSON string
customer_asset_attributes_instance = CustomerAssetAttributes.from_json(json)
# print the JSON string representation of the object
print
CustomerAssetAttributes.to_json()

# convert the object into a dict
customer_asset_attributes_dict = customer_asset_attributes_instance.to_dict()
# create an instance of CustomerAssetAttributes from a dict
customer_asset_attributes_form_dict = customer_asset_attributes.from_dict(customer_asset_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


