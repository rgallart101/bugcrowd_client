# CustomerAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 
**attributes** | [**CustomerAssetAttributes**](CustomerAssetAttributes.md) |  | 
**relationships** | [**CustomerAssetRelationships**](CustomerAssetRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.customer_asset import CustomerAsset

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerAsset from a JSON string
customer_asset_instance = CustomerAsset.from_json(json)
# print the JSON string representation of the object
print
CustomerAsset.to_json()

# convert the object into a dict
customer_asset_dict = customer_asset_instance.to_dict()
# create an instance of CustomerAsset from a dict
customer_asset_form_dict = customer_asset.from_dict(customer_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


