# CreateMonetaryRewardRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | [**CreateMonetaryRewardRequestDataAttributes**](CreateMonetaryRewardRequestDataAttributes.md) |  | [optional] 
**relationships** | [**CreateMonetaryRewardRequestDataRelationships**](CreateMonetaryRewardRequestDataRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.create_monetary_reward_request_data import CreateMonetaryRewardRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMonetaryRewardRequestData from a JSON string
create_monetary_reward_request_data_instance = CreateMonetaryRewardRequestData.from_json(json)
# print the JSON string representation of the object
print
CreateMonetaryRewardRequestData.to_json()

# convert the object into a dict
create_monetary_reward_request_data_dict = create_monetary_reward_request_data_instance.to_dict()
# create an instance of CreateMonetaryRewardRequestData from a dict
create_monetary_reward_request_data_form_dict = create_monetary_reward_request_data.from_dict(
    create_monetary_reward_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


