# UpdateMonetaryRewardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UpdateMonetaryRewardRequestData**](UpdateMonetaryRewardRequestData.md) |  | 

## Example

```python
from bugcrowd_client.models.update_monetary_reward_request import UpdateMonetaryRewardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMonetaryRewardRequest from a JSON string
update_monetary_reward_request_instance = UpdateMonetaryRewardRequest.from_json(json)
# print the JSON string representation of the object
print
UpdateMonetaryRewardRequest.to_json()

# convert the object into a dict
update_monetary_reward_request_dict = update_monetary_reward_request_instance.to_dict()
# create an instance of UpdateMonetaryRewardRequest from a dict
update_monetary_reward_request_form_dict = update_monetary_reward_request.from_dict(update_monetary_reward_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


