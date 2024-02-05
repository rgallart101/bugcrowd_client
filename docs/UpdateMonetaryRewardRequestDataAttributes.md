# UpdateMonetaryRewardRequestDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelled** | **bool** |  | 
**cancellation_comment** | **str** |  | [optional] 
**cancellation_reason** | [**MonetaryRewardCancellationReasonEnum**](MonetaryRewardCancellationReasonEnum.md) |  | 

## Example

```python
from bugcrowd_client.models.update_monetary_reward_request_data_attributes import
    UpdateMonetaryRewardRequestDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMonetaryRewardRequestDataAttributes from a JSON string
update_monetary_reward_request_data_attributes_instance = UpdateMonetaryRewardRequestDataAttributes.from_json(json)
# print the JSON string representation of the object
print
UpdateMonetaryRewardRequestDataAttributes.to_json()

# convert the object into a dict
update_monetary_reward_request_data_attributes_dict = update_monetary_reward_request_data_attributes_instance.to_dict()
# create an instance of UpdateMonetaryRewardRequestDataAttributes from a dict
update_monetary_reward_request_data_attributes_form_dict = update_monetary_reward_request_data_attributes.from_dict(
    update_monetary_reward_request_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


