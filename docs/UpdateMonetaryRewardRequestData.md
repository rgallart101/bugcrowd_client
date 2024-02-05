# UpdateMonetaryRewardRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | [**UpdateMonetaryRewardRequestDataAttributes**](UpdateMonetaryRewardRequestDataAttributes.md) |  | 

## Example

```python
from bugcrowd_client.models.update_monetary_reward_request_data import UpdateMonetaryRewardRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMonetaryRewardRequestData from a JSON string
update_monetary_reward_request_data_instance = UpdateMonetaryRewardRequestData.from_json(json)
# print the JSON string representation of the object
print
UpdateMonetaryRewardRequestData.to_json()

# convert the object into a dict
update_monetary_reward_request_data_dict = update_monetary_reward_request_data_instance.to_dict()
# create an instance of UpdateMonetaryRewardRequestData from a dict
update_monetary_reward_request_data_form_dict = update_monetary_reward_request_data.from_dict(
    update_monetary_reward_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


