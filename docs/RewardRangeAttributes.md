# RewardRangeAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**p1_max_cents** | **int** | The maximum reward for a valid P1 submission | [optional] 
**p1_min_cents** | **int** | The minimum reward for a valid P1 submission | [optional] 
**p2_max_cents** | **int** | The maximum reward for a valid P2 submission | [optional] 
**p2_min_cents** | **int** | The minimum reward for a valid P2 submission | [optional] 
**p3_max_cents** | **int** | The maximum reward for a valid P3 submission | [optional] 
**p3_min_cents** | **int** | The minimum reward for a valid P3 submission | [optional] 
**p4_max_cents** | **int** | The maximum reward for a valid P4 submission | [optional] 
**p4_min_cents** | **int** | The minimum reward for a valid P4 submission | [optional] 
**p5_max_cents** | **int** | The maximum reward for a valid P5 submission | [optional] 
**p5_min_cents** | **int** | The minimum reward for a valid P5 submission | [optional] 
**program_max_cents** | **int** | Optional maximum amount the program would pay for an exceptional submission | [optional] 

## Example

```python
from bugcrowd_client.models.reward_range_attributes import RewardRangeAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of RewardRangeAttributes from a JSON string
reward_range_attributes_instance = RewardRangeAttributes.from_json(json)
# print the JSON string representation of the object
print
RewardRangeAttributes.to_json()

# convert the object into a dict
reward_range_attributes_dict = reward_range_attributes_instance.to_dict()
# create an instance of RewardRangeAttributes from a dict
reward_range_attributes_form_dict = reward_range_attributes.from_dict(reward_range_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


