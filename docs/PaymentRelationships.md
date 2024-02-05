# PaymentRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monetary_reward** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 
**researcher** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.payment_relationships import PaymentRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRelationships from a JSON string
payment_relationships_instance = PaymentRelationships.from_json(json)
# print the JSON string representation of the object
print
PaymentRelationships.to_json()

# convert the object into a dict
payment_relationships_dict = payment_relationships_instance.to_dict()
# create an instance of PaymentRelationships from a dict
payment_relationships_form_dict = payment_relationships.from_dict(payment_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


