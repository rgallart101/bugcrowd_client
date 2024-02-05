# ListCustomerAssetsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CustomerAsset]**](CustomerAsset.md) |  | 
**meta** | [**RelationshipCountMetaData**](RelationshipCountMetaData.md) |  | [optional] 
**links** | [**NavLinks**](NavLinks.md) |  | 

## Example

```python
from bugcrowd_client.models.list_customer_assets_response import ListCustomerAssetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListCustomerAssetsResponse from a JSON string
list_customer_assets_response_instance = ListCustomerAssetsResponse.from_json(json)
# print the JSON string representation of the object
print
ListCustomerAssetsResponse.to_json()

# convert the object into a dict
list_customer_assets_response_dict = list_customer_assets_response_instance.to_dict()
# create an instance of ListCustomerAssetsResponse from a dict
list_customer_assets_response_form_dict = list_customer_assets_response.from_dict(list_customer_assets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


