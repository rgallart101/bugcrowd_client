# CustomerAssetRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 
**last_modified_by** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 
**organization** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.customer_asset_relationships import CustomerAssetRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerAssetRelationships from a JSON string
customer_asset_relationships_instance = CustomerAssetRelationships.from_json(json)
# print the JSON string representation of the object
print
CustomerAssetRelationships.to_json()

# convert the object into a dict
customer_asset_relationships_dict = customer_asset_relationships_instance.to_dict()
# create an instance of CustomerAssetRelationships from a dict
customer_asset_relationships_form_dict = customer_asset_relationships.from_dict(customer_asset_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


