# CreateMonetaryRewardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateMonetaryRewardRequestData**](CreateMonetaryRewardRequestData.md) |  | 

## Example

```python
from bugcrowd_client.models.create_monetary_reward_request import CreateMonetaryRewardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMonetaryRewardRequest from a JSON string
create_monetary_reward_request_instance = CreateMonetaryRewardRequest.from_json(json)
# print the JSON string representation of the object
print
CreateMonetaryRewardRequest.to_json()

# convert the object into a dict
create_monetary_reward_request_dict = create_monetary_reward_request_instance.to_dict()
# create an instance of CreateMonetaryRewardRequest from a dict
create_monetary_reward_request_form_dict = create_monetary_reward_request.from_dict(create_monetary_reward_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


