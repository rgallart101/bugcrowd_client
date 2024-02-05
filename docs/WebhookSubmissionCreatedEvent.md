# WebhookSubmissionCreatedEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**attributes** | [**WebhookSubmissionCreatedEventAttributes**](WebhookSubmissionCreatedEventAttributes.md) |  | 
**relationships** | [**WebhookSubmissionCreatedEventRelationships**](WebhookSubmissionCreatedEventRelationships.md) |  | 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.webhook_submission_created_event import WebhookSubmissionCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubmissionCreatedEvent from a JSON string
webhook_submission_created_event_instance = WebhookSubmissionCreatedEvent.from_json(json)
# print the JSON string representation of the object
print
WebhookSubmissionCreatedEvent.to_json()

# convert the object into a dict
webhook_submission_created_event_dict = webhook_submission_created_event_instance.to_dict()
# create an instance of WebhookSubmissionCreatedEvent from a dict
webhook_submission_created_event_form_dict = webhook_submission_created_event.from_dict(
    webhook_submission_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


