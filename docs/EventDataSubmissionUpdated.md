# EventDataSubmissionUpdated

submission.updated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**EventDataSubmissionUpdatedChanges**](EventDataSubmissionUpdatedChanges.md) |  | 
**duplicate_ids** | **List[str]** |  | 

## Example

```python
from bugcrowd_client.models.event_data_submission_updated import EventDataSubmissionUpdated

# TODO update the JSON string below
json = "{}"
# create an instance of EventDataSubmissionUpdated from a JSON string
event_data_submission_updated_instance = EventDataSubmissionUpdated.from_json(json)
# print the JSON string representation of the object
print
EventDataSubmissionUpdated.to_json()

# convert the object into a dict
event_data_submission_updated_dict = event_data_submission_updated_instance.to_dict()
# create an instance of EventDataSubmissionUpdated from a dict
event_data_submission_updated_form_dict = event_data_submission_updated.from_dict(event_data_submission_updated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


