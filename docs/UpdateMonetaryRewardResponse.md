# UpdateMonetaryRewardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MonetaryReward**](MonetaryReward.md) |  | 

## Example

```python
from bugcrowd_client.models.update_monetary_reward_response import UpdateMonetaryRewardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMonetaryRewardResponse from a JSON string
update_monetary_reward_response_instance = UpdateMonetaryRewardResponse.from_json(json)
# print the JSON string representation of the object
print
UpdateMonetaryRewardResponse.to_json()

# convert the object into a dict
update_monetary_reward_response_dict = update_monetary_reward_response_instance.to_dict()
# create an instance of UpdateMonetaryRewardResponse from a dict
update_monetary_reward_response_form_dict = update_monetary_reward_response.from_dict(
    update_monetary_reward_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


