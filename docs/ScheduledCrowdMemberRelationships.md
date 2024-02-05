# ScheduledCrowdMemberRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.scheduled_crowd_member_relationships import ScheduledCrowdMemberRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledCrowdMemberRelationships from a JSON string
scheduled_crowd_member_relationships_instance = ScheduledCrowdMemberRelationships.from_json(json)
# print the JSON string representation of the object
print
ScheduledCrowdMemberRelationships.to_json()

# convert the object into a dict
scheduled_crowd_member_relationships_dict = scheduled_crowd_member_relationships_instance.to_dict()
# create an instance of ScheduledCrowdMemberRelationships from a dict
scheduled_crowd_member_relationships_form_dict = scheduled_crowd_member_relationships.from_dict(
    scheduled_crowd_member_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


