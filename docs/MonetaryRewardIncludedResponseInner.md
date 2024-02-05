# MonetaryRewardIncludedResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | 
**attributes** | [**PaymentAttributes**](PaymentAttributes.md) |  | [optional] 
**relationships** | [**PaymentRelationships**](PaymentRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.monetary_reward_included_response_inner import MonetaryRewardIncludedResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of MonetaryRewardIncludedResponseInner from a JSON string
monetary_reward_included_response_inner_instance = MonetaryRewardIncludedResponseInner.from_json(json)
# print the JSON string representation of the object
print
MonetaryRewardIncludedResponseInner.to_json()

# convert the object into a dict
monetary_reward_included_response_inner_dict = monetary_reward_included_response_inner_instance.to_dict()
# create an instance of MonetaryRewardIncludedResponseInner from a dict
monetary_reward_included_response_inner_form_dict = monetary_reward_included_response_inner.from_dict(
    monetary_reward_included_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


