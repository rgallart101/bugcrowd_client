# CreateCustomerAssetRequestDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the asset. | 
**type** | **str** | Basic categorization that defines the type of the asset. | 
**description** | **str** | A brief description of your asset. | [optional] 
**host_name** | **str** |  | [optional] 
**port_list** | **List[int]** | A list of port numbers for the asset between the range of 1 to 65535. | [optional] 
**ip_address** | **List[str]** | A list of IPv4 / IPv6 / CIDR range of IP Address for the asset. | [optional] 
**approved** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**attributes** | **Dict[object]** | An array of key value pairs of all possible attributes for the asset. The &#x60;key&#x60; holds the name for the asset_attribute and the &#x60;value&#x60; to holds value for its respective key.  Commonly expected attributes are &#x60;external_id, external_link, record_type, autonomous_system_number etc&#x60;.  If attribute name is &#x60;record_type&#x60;, then it should match one of the values in &#x60;A AAAA PTR CNAME MX TXT NS SOA SRV&#x60;.  If attribute name is &#x60;autonomous_system_number&#x60;, then they should be unique 16 bit numbers between 1 and 65534 or 32 bit numbers between 131072 and 4294967294. They are presented in format: AS(number).  If attribute name is &#x60;external-id&#x60;, then it is often a Configuration Item ID from a CMDB. Sometimes this is an ID from an external discovery scanner tool.  If attribute name is &#x60;external-link&#x60;, then it is a hyperlink or identifier.  Customers can also specify their own attributes other than the given above list.  | [optional] 
**tags** | [**CreateCustomerAssetRequestDataAttributesTags**](CreateCustomerAssetRequestDataAttributesTags.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.create_customer_asset_request_data_attributes import
    CreateCustomerAssetRequestDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomerAssetRequestDataAttributes from a JSON string
create_customer_asset_request_data_attributes_instance = CreateCustomerAssetRequestDataAttributes.from_json(json)
# print the JSON string representation of the object
print
CreateCustomerAssetRequestDataAttributes.to_json()

# convert the object into a dict
create_customer_asset_request_data_attributes_dict = create_customer_asset_request_data_attributes_instance.to_dict()
# create an instance of CreateCustomerAssetRequestDataAttributes from a dict
create_customer_asset_request_data_attributes_form_dict = create_customer_asset_request_data_attributes.from_dict(
    create_customer_asset_request_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


