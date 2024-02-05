# ScheduledCrowdMemberAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the scheduled crowd member | [optional] 
**accepted_at** | **datetime** | Time at which the invitation was accepted | [optional] 

## Example

```python
from bugcrowd_client.models.scheduled_crowd_member_attributes import ScheduledCrowdMemberAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledCrowdMemberAttributes from a JSON string
scheduled_crowd_member_attributes_instance = ScheduledCrowdMemberAttributes.from_json(json)
# print the JSON string representation of the object
print
ScheduledCrowdMemberAttributes.to_json()

# convert the object into a dict
scheduled_crowd_member_attributes_dict = scheduled_crowd_member_attributes_instance.to_dict()
# create an instance of ScheduledCrowdMemberAttributes from a dict
scheduled_crowd_member_attributes_form_dict = scheduled_crowd_member_attributes.from_dict(
    scheduled_crowd_member_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


