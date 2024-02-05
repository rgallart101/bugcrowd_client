# CreateRewardRangeRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | [**CreateRewardRangeRequestDataAttributes**](CreateRewardRangeRequestDataAttributes.md) |  | 

## Example

```python
from bugcrowd_client.models.create_reward_range_request_data import CreateRewardRangeRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRewardRangeRequestData from a JSON string
create_reward_range_request_data_instance = CreateRewardRangeRequestData.from_json(json)
# print the JSON string representation of the object
print
CreateRewardRangeRequestData.to_json()

# convert the object into a dict
create_reward_range_request_data_dict = create_reward_range_request_data_instance.to_dict()
# create an instance of CreateRewardRangeRequestData from a dict
create_reward_range_request_data_form_dict = create_reward_range_request_data.from_dict(
    create_reward_range_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


