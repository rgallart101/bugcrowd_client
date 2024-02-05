# GetScheduledCrowdMemberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ScheduledCrowdMember**](ScheduledCrowdMember.md) |  | 
**included** | [**List[ScheduledCrowdMemberIncludeResponseInner]**](ScheduledCrowdMemberIncludeResponseInner.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.get_scheduled_crowd_member_response import GetScheduledCrowdMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetScheduledCrowdMemberResponse from a JSON string
get_scheduled_crowd_member_response_instance = GetScheduledCrowdMemberResponse.from_json(json)
# print the JSON string representation of the object
print
GetScheduledCrowdMemberResponse.to_json()

# convert the object into a dict
get_scheduled_crowd_member_response_dict = get_scheduled_crowd_member_response_instance.to_dict()
# create an instance of GetScheduledCrowdMemberResponse from a dict
get_scheduled_crowd_member_response_form_dict = get_scheduled_crowd_member_response.from_dict(
    get_scheduled_crowd_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


