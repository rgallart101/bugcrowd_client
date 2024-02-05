# UpdateCustomerAssetRequestDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name for your asset. | [optional] 
**type** | **str** | To hold type of the customer asset to be updated with. It should contain only one of the enum values specified below.  | [optional] 
**description** | **str** |  | [optional] 
**host_name** | **str** |  | [optional] 
**port_list** | **List[int]** | A list of port numbers for the asset between the range of 1 to 65535. Note - Update will replace any previously added ports.  | [optional] 
**ip_address** | **List[str]** | A list of IPv4 / IPv6 / CIDR range of IP Address for the asset. Note - Update will replace any previously added IP Address.  | [optional] 
**attributes** | **Dict[object]** | To hold an array of asset_attributes which are basically key-value pairs of all possible attributes for the asset. The &#x60;key&#x60; to hold the name for the asset_attribute and the &#x60;value&#x60; to holds its value.  Commonly expected attributes are &#x60;external_id, external_link, record_type, autonomous_system_number etc&#x60;.  If the key is &#x60;record_type&#x60;, then its value should be in &#x60;A, AAAA, PTR, CNAME, MX, TXT, NS, SOA and SRV&#x60;.  If the key is &#x60;autonomous_system_number&#x60;, then it should be a unique 16 bit numbers between 1 and 65534 or 32 bit numbers between 131072 and 4294967294. The number should be prefixed with AS. Example - AS(number).  External ID is often a Configuration Item ID from a CMDB. Sometimes this is an ID from an external discovery scanner tool.  External link is a hyperlink or an identifier.  Customers can also specify their own attributes other than the given above list.Update will replace the entire list of previously added asset_attributes with list specified here.  | [optional] 
**approved** | **bool** | Specifies if the asset is user approved and ready to be used. | [optional] 
**tags** | [**UpdateCustomerAssetRequestDataAttributesTags**](UpdateCustomerAssetRequestDataAttributesTags.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.update_customer_asset_request_data_attributes import
    UpdateCustomerAssetRequestDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomerAssetRequestDataAttributes from a JSON string
update_customer_asset_request_data_attributes_instance = UpdateCustomerAssetRequestDataAttributes.from_json(json)
# print the JSON string representation of the object
print
UpdateCustomerAssetRequestDataAttributes.to_json()

# convert the object into a dict
update_customer_asset_request_data_attributes_dict = update_customer_asset_request_data_attributes_instance.to_dict()
# create an instance of UpdateCustomerAssetRequestDataAttributes from a dict
update_customer_asset_request_data_attributes_form_dict = update_customer_asset_request_data_attributes.from_dict(
    update_customer_asset_request_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


