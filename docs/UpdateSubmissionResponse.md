# UpdateSubmissionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Submission**](Submission.md) |  | 

## Example

```python
from bugcrowd_client.models.update_submission_response import UpdateSubmissionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubmissionResponse from a JSON string
update_submission_response_instance = UpdateSubmissionResponse.from_json(json)
# print the JSON string representation of the object
print
UpdateSubmissionResponse.to_json()

# convert the object into a dict
update_submission_response_dict = update_submission_response_instance.to_dict()
# create an instance of UpdateSubmissionResponse from a dict
update_submission_response_form_dict = update_submission_response.from_dict(update_submission_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


