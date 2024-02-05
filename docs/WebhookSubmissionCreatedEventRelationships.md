# WebhookSubmissionCreatedEventRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor** | [**WebhookSubmissionCreatedEventRelationshipsActor**](WebhookSubmissionCreatedEventRelationshipsActor.md) |  | 
**resource** | [**WebhookSubmissionCreatedEventRelationshipsResource**](WebhookSubmissionCreatedEventRelationshipsResource.md) |  | 

## Example

```python
from bugcrowd_client.models.webhook_submission_created_event_relationships import
    WebhookSubmissionCreatedEventRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubmissionCreatedEventRelationships from a JSON string
webhook_submission_created_event_relationships_instance = WebhookSubmissionCreatedEventRelationships.from_json(json)
# print the JSON string representation of the object
print
WebhookSubmissionCreatedEventRelationships.to_json()

# convert the object into a dict
webhook_submission_created_event_relationships_dict = webhook_submission_created_event_relationships_instance.to_dict()
# create an instance of WebhookSubmissionCreatedEventRelationships from a dict
webhook_submission_created_event_relationships_form_dict = webhook_submission_created_event_relationships.from_dict(
    webhook_submission_created_event_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


