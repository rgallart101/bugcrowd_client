# WebhookSubmissionCreatedEventAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**key** | **str** |  | 
**data** | [**EventDataSubmissionCreated**](EventDataSubmissionCreated.md) |  | 

## Example

```python
from bugcrowd_client.models.webhook_submission_created_event_attributes import WebhookSubmissionCreatedEventAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubmissionCreatedEventAttributes from a JSON string
webhook_submission_created_event_attributes_instance = WebhookSubmissionCreatedEventAttributes.from_json(json)
# print the JSON string representation of the object
print
WebhookSubmissionCreatedEventAttributes.to_json()

# convert the object into a dict
webhook_submission_created_event_attributes_dict = webhook_submission_created_event_attributes_instance.to_dict()
# create an instance of WebhookSubmissionCreatedEventAttributes from a dict
webhook_submission_created_event_attributes_form_dict = webhook_submission_created_event_attributes.from_dict(
    webhook_submission_created_event_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


