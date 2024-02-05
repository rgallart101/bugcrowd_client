# GetSubmissionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Submission**](Submission.md) |  | 
**included** | [**List[SubmissionIncludedResponseInner]**](SubmissionIncludedResponseInner.md) |  | [optional] 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.get_submission_response import GetSubmissionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubmissionResponse from a JSON string
get_submission_response_instance = GetSubmissionResponse.from_json(json)
# print the JSON string representation of the object
print
GetSubmissionResponse.to_json()

# convert the object into a dict
get_submission_response_dict = get_submission_response_instance.to_dict()
# create an instance of GetSubmissionResponse from a dict
get_submission_response_form_dict = get_submission_response.from_dict(get_submission_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


