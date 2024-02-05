# CustomerAssetAttributesAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Indicates the key or name of the asset_attribute. | [optional] 
**value** | **str** | Indicates the value of the asset_attribute for a given key. | [optional] 

## Example

```python
from bugcrowd_client.models.customer_asset_attributes_attributes_inner import CustomerAssetAttributesAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerAssetAttributesAttributesInner from a JSON string
customer_asset_attributes_attributes_inner_instance = CustomerAssetAttributesAttributesInner.from_json(json)
# print the JSON string representation of the object
print
CustomerAssetAttributesAttributesInner.to_json()

# convert the object into a dict
customer_asset_attributes_attributes_inner_dict = customer_asset_attributes_attributes_inner_instance.to_dict()
# create an instance of CustomerAssetAttributesAttributesInner from a dict
customer_asset_attributes_attributes_inner_form_dict = customer_asset_attributes_attributes_inner.from_dict(
    customer_asset_attributes_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


