# WebhookSubmissionCreatedEventRelationshipsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WebhookSubmissionCreatedEventRelationshipsResourceData**](WebhookSubmissionCreatedEventRelationshipsResourceData.md) |  | 
**links** | [**SingleRelationshipLinks**](SingleRelationshipLinks.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.webhook_submission_created_event_relationships_resource import
    WebhookSubmissionCreatedEventRelationshipsResource

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubmissionCreatedEventRelationshipsResource from a JSON string
webhook_submission_created_event_relationships_resource_instance = WebhookSubmissionCreatedEventRelationshipsResource.from_json(
    json)
# print the JSON string representation of the object
print
WebhookSubmissionCreatedEventRelationshipsResource.to_json()

# convert the object into a dict
webhook_submission_created_event_relationships_resource_dict = webhook_submission_created_event_relationships_resource_instance.to_dict()
# create an instance of WebhookSubmissionCreatedEventRelationshipsResource from a dict
webhook_submission_created_event_relationships_resource_form_dict = webhook_submission_created_event_relationships_resource.from_dict(
    webhook_submission_created_event_relationships_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


