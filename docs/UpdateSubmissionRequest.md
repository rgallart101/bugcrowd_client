# UpdateSubmissionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UpdateSubmissionRequestData**](UpdateSubmissionRequestData.md) |  | 

## Example

```python
from bugcrowd_client.models.update_submission_request import UpdateSubmissionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubmissionRequest from a JSON string
update_submission_request_instance = UpdateSubmissionRequest.from_json(json)
# print the JSON string representation of the object
print
UpdateSubmissionRequest.to_json()

# convert the object into a dict
update_submission_request_dict = update_submission_request_instance.to_dict()
# create an instance of UpdateSubmissionRequest from a dict
update_submission_request_form_dict = update_submission_request.from_dict(update_submission_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


