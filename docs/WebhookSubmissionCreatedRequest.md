# WebhookSubmissionCreatedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WebhookSubmissionCreatedEvent**](WebhookSubmissionCreatedEvent.md) |  | 
**included** | [**List[WebhookSubmissionCreatedRequestIncludedInner]**](WebhookSubmissionCreatedRequestIncludedInner.md) |  | 

## Example

```python
from bugcrowd_client.models.webhook_submission_created_request import WebhookSubmissionCreatedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubmissionCreatedRequest from a JSON string
webhook_submission_created_request_instance = WebhookSubmissionCreatedRequest.from_json(json)
# print the JSON string representation of the object
print
WebhookSubmissionCreatedRequest.to_json()

# convert the object into a dict
webhook_submission_created_request_dict = webhook_submission_created_request_instance.to_dict()
# create an instance of WebhookSubmissionCreatedRequest from a dict
webhook_submission_created_request_form_dict = webhook_submission_created_request.from_dict(
    webhook_submission_created_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


