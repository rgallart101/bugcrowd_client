# PaymentAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_cents** | **int** | Amount of the reward specified in cents | [optional] 
**created_at** | **str** | Time at which the object was created | [optional] 
**remitted_at** | **str** | Time at which the reward was remitted | [optional] 

## Example

```python
from bugcrowd_client.models.payment_attributes import PaymentAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAttributes from a JSON string
payment_attributes_instance = PaymentAttributes.from_json(json)
# print the JSON string representation of the object
print
PaymentAttributes.to_json()

# convert the object into a dict
payment_attributes_dict = payment_attributes_instance.to_dict()
# create an instance of PaymentAttributes from a dict
payment_attributes_form_dict = payment_attributes.from_dict(payment_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


