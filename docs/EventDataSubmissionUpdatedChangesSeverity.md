# EventDataSubmissionUpdatedChangesSeverity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **int** |  | [optional] 
**to** | **int** |  | [optional] 

## Example

```python
from bugcrowd_client.models.event_data_submission_updated_changes_severity import
    EventDataSubmissionUpdatedChangesSeverity

# TODO update the JSON string below
json = "{}"
# create an instance of EventDataSubmissionUpdatedChangesSeverity from a JSON string
event_data_submission_updated_changes_severity_instance = EventDataSubmissionUpdatedChangesSeverity.from_json(json)
# print the JSON string representation of the object
print
EventDataSubmissionUpdatedChangesSeverity.to_json()

# convert the object into a dict
event_data_submission_updated_changes_severity_dict = event_data_submission_updated_changes_severity_instance.to_dict()
# create an instance of EventDataSubmissionUpdatedChangesSeverity from a dict
event_data_submission_updated_changes_severity_form_dict = event_data_submission_updated_changes_severity.from_dict(
    event_data_submission_updated_changes_severity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


