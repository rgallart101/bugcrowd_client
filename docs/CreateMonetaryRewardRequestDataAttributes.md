# CreateMonetaryRewardRequestDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_cents** | **int** |  | 
**comment** | **str** |  | [optional] 

## Example

```python
from bugcrowd_client.models.create_monetary_reward_request_data_attributes import
    CreateMonetaryRewardRequestDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMonetaryRewardRequestDataAttributes from a JSON string
create_monetary_reward_request_data_attributes_instance = CreateMonetaryRewardRequestDataAttributes.from_json(json)
# print the JSON string representation of the object
print
CreateMonetaryRewardRequestDataAttributes.to_json()

# convert the object into a dict
create_monetary_reward_request_data_attributes_dict = create_monetary_reward_request_data_attributes_instance.to_dict()
# create an instance of CreateMonetaryRewardRequestDataAttributes from a dict
create_monetary_reward_request_data_attributes_form_dict = create_monetary_reward_request_data_attributes.from_dict(
    create_monetary_reward_request_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


