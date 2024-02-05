# ListScheduledCrowdMemberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ScheduledCrowdMember]**](ScheduledCrowdMember.md) |  | 
**included** | [**List[ScheduledCrowdMemberIncludeResponseInner]**](ScheduledCrowdMemberIncludeResponseInner.md) |  | [optional] 
**meta** | [**RelationshipCountMetaData**](RelationshipCountMetaData.md) |  | [optional] 
**links** | [**NavLinks**](NavLinks.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.list_scheduled_crowd_member_response import ListScheduledCrowdMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListScheduledCrowdMemberResponse from a JSON string
list_scheduled_crowd_member_response_instance = ListScheduledCrowdMemberResponse.from_json(json)
# print the JSON string representation of the object
print
ListScheduledCrowdMemberResponse.to_json()

# convert the object into a dict
list_scheduled_crowd_member_response_dict = list_scheduled_crowd_member_response_instance.to_dict()
# create an instance of ListScheduledCrowdMemberResponse from a dict
list_scheduled_crowd_member_response_form_dict = list_scheduled_crowd_member_response.from_dict(
    list_scheduled_crowd_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


