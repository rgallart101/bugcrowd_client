# MonetaryRewardAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_cents** | **int** | Amount of the monetary reward specified in cents | [optional] 
**cancellation_comment** | **str** | Optional comment provided when a monetary reward has been canceled | [optional] 
**cancellation_reason** | [**NullableMonetaryRewardCancellationReasonEnum**](NullableMonetaryRewardCancellationReasonEnum.md) |  | [optional] 
**cancelled_at** | **str** | Timestamp indicating when a monetary reward was cancelled | [optional] 
**cancelled** | **bool** | Boolean indicating whether a monetary reward has been cancelled | [optional] 
**comment** | **str** | Comment regarding monetary reward. This is mostly optional, but required if a reward is outside the range associated with the assigned priority | [optional] 
**created_at** | **str** | Time at which the object was created | [optional] 
**reason** | [**MonetaryRewardReasonEnum**](MonetaryRewardReasonEnum.md) |  | [optional] 
**rewarded_at** | **str** | Time at which the object was rewarded | [optional] 
**formatted_amount** | **str** | Monetary reward amount formatted is UDS with dollars and cents. Example: $1,234.56 | [optional] 

## Example

```python
from bugcrowd_client.models.monetary_reward_attributes import MonetaryRewardAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of MonetaryRewardAttributes from a JSON string
monetary_reward_attributes_instance = MonetaryRewardAttributes.from_json(json)
# print the JSON string representation of the object
print
MonetaryRewardAttributes.to_json()

# convert the object into a dict
monetary_reward_attributes_dict = monetary_reward_attributes_instance.to_dict()
# create an instance of MonetaryRewardAttributes from a dict
monetary_reward_attributes_form_dict = monetary_reward_attributes.from_dict(monetary_reward_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


