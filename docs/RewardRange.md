# RewardRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 
**attributes** | [**RewardRangeAttributes**](RewardRangeAttributes.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from bugcrowd_client.models.reward_range import RewardRange

# TODO update the JSON string below
json = "{}"
# create an instance of RewardRange from a JSON string
reward_range_instance = RewardRange.from_json(json)
# print the JSON string representation of the object
print
RewardRange.to_json()

# convert the object into a dict
reward_range_dict = reward_range_instance.to_dict()
# create an instance of RewardRange from a dict
reward_range_form_dict = reward_range.from_dict(reward_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


