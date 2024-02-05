# ScheduledCrowdMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 
**attributes** | [**ScheduledCrowdMemberAttributes**](ScheduledCrowdMemberAttributes.md) |  | [optional] 
**relationships** | [**ScheduledCrowdMemberRelationships**](ScheduledCrowdMemberRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.scheduled_crowd_member import ScheduledCrowdMember

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledCrowdMember from a JSON string
scheduled_crowd_member_instance = ScheduledCrowdMember.from_json(json)
# print the JSON string representation of the object
print
ScheduledCrowdMember.to_json()

# convert the object into a dict
scheduled_crowd_member_dict = scheduled_crowd_member_instance.to_dict()
# create an instance of ScheduledCrowdMember from a dict
scheduled_crowd_member_form_dict = scheduled_crowd_member.from_dict(scheduled_crowd_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


