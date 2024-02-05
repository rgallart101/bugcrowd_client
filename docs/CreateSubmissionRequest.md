# CreateSubmissionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateSubmissionRequestData**](CreateSubmissionRequestData.md) |  | 

## Example

```python
from bugcrowd_client.models.create_submission_request import CreateSubmissionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubmissionRequest from a JSON string
create_submission_request_instance = CreateSubmissionRequest.from_json(json)
# print the JSON string representation of the object
print
CreateSubmissionRequest.to_json()

# convert the object into a dict
create_submission_request_dict = create_submission_request_instance.to_dict()
# create an instance of CreateSubmissionRequest from a dict
create_submission_request_form_dict = create_submission_request.from_dict(create_submission_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


