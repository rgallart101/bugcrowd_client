# ScheduledCrowdMemberIncludeResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**attributes** | [**ProgramDocusignUserAttributes**](ProgramDocusignUserAttributes.md) |  | [optional] 
**relationships** | [**UserRelationships**](UserRelationships.md) |  | [optional] 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.scheduled_crowd_member_include_response_inner import
    ScheduledCrowdMemberIncludeResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledCrowdMemberIncludeResponseInner from a JSON string
scheduled_crowd_member_include_response_inner_instance = ScheduledCrowdMemberIncludeResponseInner.from_json(json)
# print the JSON string representation of the object
print
ScheduledCrowdMemberIncludeResponseInner.to_json()

# convert the object into a dict
scheduled_crowd_member_include_response_inner_dict = scheduled_crowd_member_include_response_inner_instance.to_dict()
# create an instance of ScheduledCrowdMemberIncludeResponseInner from a dict
scheduled_crowd_member_include_response_inner_form_dict = scheduled_crowd_member_include_response_inner.from_dict(
    scheduled_crowd_member_include_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


