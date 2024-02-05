# Payment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 
**attributes** | [**PaymentAttributes**](PaymentAttributes.md) |  | [optional] 
**relationships** | [**PaymentRelationships**](PaymentRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.payment import Payment

# TODO update the JSON string below
json = "{}"
# create an instance of Payment from a JSON string
payment_instance = Payment.from_json(json)
# print the JSON string representation of the object
print
Payment.to_json()

# convert the object into a dict
payment_dict = payment_instance.to_dict()
# create an instance of Payment from a dict
payment_form_dict = payment.from_dict(payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


