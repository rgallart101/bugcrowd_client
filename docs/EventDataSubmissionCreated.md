# EventDataSubmissionCreated

submission.created

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**current_substate** | **str** |  | [optional] 

## Example

```python
from bugcrowd_client.models.event_data_submission_created import EventDataSubmissionCreated

# TODO update the JSON string below
json = "{}"
# create an instance of EventDataSubmissionCreated from a JSON string
event_data_submission_created_instance = EventDataSubmissionCreated.from_json(json)
# print the JSON string representation of the object
print
EventDataSubmissionCreated.to_json()

# convert the object into a dict
event_data_submission_created_dict = event_data_submission_created_instance.to_dict()
# create an instance of EventDataSubmissionCreated from a dict
event_data_submission_created_form_dict = event_data_submission_created.from_dict(event_data_submission_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


