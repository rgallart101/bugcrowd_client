# CreateRewardRangeRequestDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**p1_max_cents** | **int** |  | [optional] 
**p1_min_cents** | **int** |  | [optional] 
**p2_max_cents** | **int** |  | [optional] 
**p2_min_cents** | **int** |  | [optional] 
**p3_max_cents** | **int** |  | [optional] 
**p3_min_cents** | **int** |  | [optional] 
**p4_max_cents** | **int** |  | [optional] 
**p4_min_cents** | **int** |  | [optional] 
**p5_max_cents** | **int** |  | [optional] 
**p5_min_cents** | **int** |  | [optional] 
**program_max_cents** | **int** |  | [optional] 

## Example

```python
from bugcrowd_client.models.create_reward_range_request_data_attributes import CreateRewardRangeRequestDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRewardRangeRequestDataAttributes from a JSON string
create_reward_range_request_data_attributes_instance = CreateRewardRangeRequestDataAttributes.from_json(json)
# print the JSON string representation of the object
print
CreateRewardRangeRequestDataAttributes.to_json()

# convert the object into a dict
create_reward_range_request_data_attributes_dict = create_reward_range_request_data_attributes_instance.to_dict()
# create an instance of CreateRewardRangeRequestDataAttributes from a dict
create_reward_range_request_data_attributes_form_dict = create_reward_range_request_data_attributes.from_dict(
    create_reward_range_request_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


