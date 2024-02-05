# RewardRangeNullableData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 

## Example

```python
from bugcrowd_client.models.reward_range_nullable_data import RewardRangeNullableData

# TODO update the JSON string below
json = "{}"
# create an instance of RewardRangeNullableData from a JSON string
reward_range_nullable_data_instance = RewardRangeNullableData.from_json(json)
# print the JSON string representation of the object
print
RewardRangeNullableData.to_json()

# convert the object into a dict
reward_range_nullable_data_dict = reward_range_nullable_data_instance.to_dict()
# create an instance of RewardRangeNullableData from a dict
reward_range_nullable_data_form_dict = reward_range_nullable_data.from_dict(reward_range_nullable_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


