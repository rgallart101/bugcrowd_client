# GetMonetaryRewardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MonetaryReward**](MonetaryReward.md) |  | 
**included** | [**List[MonetaryRewardIncludedResponseInner]**](MonetaryRewardIncludedResponseInner.md) |  | [optional] 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.get_monetary_reward_response import GetMonetaryRewardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMonetaryRewardResponse from a JSON string
get_monetary_reward_response_instance = GetMonetaryRewardResponse.from_json(json)
# print the JSON string representation of the object
print
GetMonetaryRewardResponse.to_json()

# convert the object into a dict
get_monetary_reward_response_dict = get_monetary_reward_response_instance.to_dict()
# create an instance of GetMonetaryRewardResponse from a dict
get_monetary_reward_response_form_dict = get_monetary_reward_response.from_dict(get_monetary_reward_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


