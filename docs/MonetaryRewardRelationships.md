# MonetaryRewardRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payments** | [**ManyRelationship**](ManyRelationship.md) |  | [optional] 
**rewarded_by** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 
**submission** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 
**cancelled_by** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.monetary_reward_relationships import MonetaryRewardRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of MonetaryRewardRelationships from a JSON string
monetary_reward_relationships_instance = MonetaryRewardRelationships.from_json(json)
# print the JSON string representation of the object
print
MonetaryRewardRelationships.to_json()

# convert the object into a dict
monetary_reward_relationships_dict = monetary_reward_relationships_instance.to_dict()
# create an instance of MonetaryRewardRelationships from a dict
monetary_reward_relationships_form_dict = monetary_reward_relationships.from_dict(monetary_reward_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


