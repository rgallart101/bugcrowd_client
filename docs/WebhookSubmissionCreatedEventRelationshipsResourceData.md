# WebhookSubmissionCreatedEventRelationshipsResourceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | Unique identifier for the resource | 

## Example

```python
from bugcrowd_client.models.webhook_submission_created_event_relationships_resource_data import
    WebhookSubmissionCreatedEventRelationshipsResourceData

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubmissionCreatedEventRelationshipsResourceData from a JSON string
webhook_submission_created_event_relationships_resource_data_instance = WebhookSubmissionCreatedEventRelationshipsResourceData.from_json(
    json)
# print the JSON string representation of the object
print
WebhookSubmissionCreatedEventRelationshipsResourceData.to_json()

# convert the object into a dict
webhook_submission_created_event_relationships_resource_data_dict = webhook_submission_created_event_relationships_resource_data_instance.to_dict()
# create an instance of WebhookSubmissionCreatedEventRelationshipsResourceData from a dict
webhook_submission_created_event_relationships_resource_data_form_dict = webhook_submission_created_event_relationships_resource_data.from_dict(
    webhook_submission_created_event_relationships_resource_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


