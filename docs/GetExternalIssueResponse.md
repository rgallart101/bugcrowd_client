# GetExternalIssueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ExternalIssue**](ExternalIssue.md) |  | 
**included** | [**List[Submission]**](Submission.md) |  | [optional] 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.get_external_issue_response import GetExternalIssueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetExternalIssueResponse from a JSON string
get_external_issue_response_instance = GetExternalIssueResponse.from_json(json)
# print the JSON string representation of the object
print
GetExternalIssueResponse.to_json()

# convert the object into a dict
get_external_issue_response_dict = get_external_issue_response_instance.to_dict()
# create an instance of GetExternalIssueResponse from a dict
get_external_issue_response_form_dict = get_external_issue_response.from_dict(get_external_issue_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


