# MonetaryReward


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 
**attributes** | [**MonetaryRewardAttributes**](MonetaryRewardAttributes.md) |  | [optional] 
**relationships** | [**MonetaryRewardRelationships**](MonetaryRewardRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.monetary_reward import MonetaryReward

# TODO update the JSON string below
json = "{}"
# create an instance of MonetaryReward from a JSON string
monetary_reward_instance = MonetaryReward.from_json(json)
# print the JSON string representation of the object
print
MonetaryReward.to_json()

# convert the object into a dict
monetary_reward_dict = monetary_reward_instance.to_dict()
# create an instance of MonetaryReward from a dict
monetary_reward_form_dict = monetary_reward.from_dict(monetary_reward_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


