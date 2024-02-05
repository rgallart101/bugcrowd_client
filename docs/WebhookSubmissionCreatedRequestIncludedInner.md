# WebhookSubmissionCreatedRequestIncludedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | 
**attributes** | [**SubmissionAttributes**](SubmissionAttributes.md) |  | [optional] 
**relationships** | [**SubmissionRelationships**](SubmissionRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.webhook_submission_created_request_included_inner import
    WebhookSubmissionCreatedRequestIncludedInner

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubmissionCreatedRequestIncludedInner from a JSON string
webhook_submission_created_request_included_inner_instance = WebhookSubmissionCreatedRequestIncludedInner.from_json(
    json)
# print the JSON string representation of the object
print
WebhookSubmissionCreatedRequestIncludedInner.to_json()

# convert the object into a dict
webhook_submission_created_request_included_inner_dict = webhook_submission_created_request_included_inner_instance.to_dict()
# create an instance of WebhookSubmissionCreatedRequestIncludedInner from a dict
webhook_submission_created_request_included_inner_form_dict = webhook_submission_created_request_included_inner.from_dict(
    webhook_submission_created_request_included_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


