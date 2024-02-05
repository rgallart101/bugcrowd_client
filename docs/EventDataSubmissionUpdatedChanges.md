# EventDataSubmissionUpdatedChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_fields** | [**Dict[str, EventDataSubmissionUpdatedChangesCustomFieldsValue]**](EventDataSubmissionUpdatedChangesCustomFieldsValue.md) |  | [optional] 
**cvss_vector_id** | [**EventDataSubmissionUpdatedChangesCvssVectorId**](EventDataSubmissionUpdatedChangesCvssVectorId.md) |  | [optional] 
**duplicate** | [**EventDataSubmissionUpdatedChangesDuplicate**](EventDataSubmissionUpdatedChangesDuplicate.md) |  | [optional] 
**duplicate_of_id** | [**EventDataSubmissionUpdatedChangesCvssVectorId**](EventDataSubmissionUpdatedChangesCvssVectorId.md) |  | [optional] 
**encrypted_bug_url** | [**EventDataSubmissionUpdatedChangesEncryptedBugUrl**](EventDataSubmissionUpdatedChangesEncryptedBugUrl.md) |  | [optional] 
**encrypted_description** | [**EventDataSubmissionUpdatedChangesEncryptedBugUrl**](EventDataSubmissionUpdatedChangesEncryptedBugUrl.md) |  | [optional] 
**encrypted_extra_info** | [**EventDataSubmissionUpdatedChangesEncryptedBugUrl**](EventDataSubmissionUpdatedChangesEncryptedBugUrl.md) |  | [optional] 
**encrypted_http_request** | [**EventDataSubmissionUpdatedChangesEncryptedBugUrl**](EventDataSubmissionUpdatedChangesEncryptedBugUrl.md) |  | [optional] 
**remediation_advice** | [**EventDataSubmissionUpdatedChangesCustomFieldsValue**](EventDataSubmissionUpdatedChangesCustomFieldsValue.md) |  | [optional] 
**remediation_advice_edited** | [**EventDataSubmissionUpdatedChangesDuplicate**](EventDataSubmissionUpdatedChangesDuplicate.md) |  | [optional] 
**target_id** | [**EventDataSubmissionUpdatedChangesCvssVectorId**](EventDataSubmissionUpdatedChangesCvssVectorId.md) |  | [optional] 
**title** | [**EventDataSubmissionUpdatedChangesTitle**](EventDataSubmissionUpdatedChangesTitle.md) |  | [optional] 
**vrt_id** | [**EventDataSubmissionUpdatedChangesCustomFieldsValue**](EventDataSubmissionUpdatedChangesCustomFieldsValue.md) |  | [optional] 
**vrt_version** | [**EventDataSubmissionUpdatedChangesTitle**](EventDataSubmissionUpdatedChangesTitle.md) |  | [optional] 
**vulnerability_references** | [**EventDataSubmissionUpdatedChangesCustomFieldsValue**](EventDataSubmissionUpdatedChangesCustomFieldsValue.md) |  | [optional] 
**vulnerability_refs_edited** | [**EventDataSubmissionUpdatedChangesDuplicate**](EventDataSubmissionUpdatedChangesDuplicate.md) |  | [optional] 
**state** | [**EventDataSubmissionUpdatedChangesCustomFieldsValue**](EventDataSubmissionUpdatedChangesCustomFieldsValue.md) |  | [optional] 
**severity** | [**EventDataSubmissionUpdatedChangesSeverity**](EventDataSubmissionUpdatedChangesSeverity.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.event_data_submission_updated_changes import EventDataSubmissionUpdatedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of EventDataSubmissionUpdatedChanges from a JSON string
event_data_submission_updated_changes_instance = EventDataSubmissionUpdatedChanges.from_json(json)
# print the JSON string representation of the object
print
EventDataSubmissionUpdatedChanges.to_json()

# convert the object into a dict
event_data_submission_updated_changes_dict = event_data_submission_updated_changes_instance.to_dict()
# create an instance of EventDataSubmissionUpdatedChanges from a dict
event_data_submission_updated_changes_form_dict = event_data_submission_updated_changes.from_dict(
    event_data_submission_updated_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


