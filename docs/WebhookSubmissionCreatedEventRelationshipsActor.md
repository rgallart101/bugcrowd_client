# WebhookSubmissionCreatedEventRelationshipsActor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EventRelationshipsActorData**](EventRelationshipsActorData.md) |  | 
**links** | [**SingleRelationshipLinks**](SingleRelationshipLinks.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.webhook_submission_created_event_relationships_actor import
    WebhookSubmissionCreatedEventRelationshipsActor

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubmissionCreatedEventRelationshipsActor from a JSON string
webhook_submission_created_event_relationships_actor_instance = WebhookSubmissionCreatedEventRelationshipsActor.from_json(
    json)
# print the JSON string representation of the object
print
WebhookSubmissionCreatedEventRelationshipsActor.to_json()

# convert the object into a dict
webhook_submission_created_event_relationships_actor_dict = webhook_submission_created_event_relationships_actor_instance.to_dict()
# create an instance of WebhookSubmissionCreatedEventRelationshipsActor from a dict
webhook_submission_created_event_relationships_actor_form_dict = webhook_submission_created_event_relationships_actor.from_dict(
    webhook_submission_created_event_relationships_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


