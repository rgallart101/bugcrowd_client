# CreateRewardRangeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateRewardRangeRequestData**](CreateRewardRangeRequestData.md) |  | 

## Example

```python
from bugcrowd_client.models.create_reward_range_request import CreateRewardRangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRewardRangeRequest from a JSON string
create_reward_range_request_instance = CreateRewardRangeRequest.from_json(json)
# print the JSON string representation of the object
print
CreateRewardRangeRequest.to_json()

# convert the object into a dict
create_reward_range_request_dict = create_reward_range_request_instance.to_dict()
# create an instance of CreateRewardRangeRequest from a dict
create_reward_range_request_form_dict = create_reward_range_request.from_dict(create_reward_range_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


