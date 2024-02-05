# ListExternalIssueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ExternalIssue]**](ExternalIssue.md) |  | 
**included** | [**List[Submission]**](Submission.md) |  | [optional] 
**links** | [**NavLinks**](NavLinks.md) |  | [optional] 
**meta** | [**RelationshipCountMetaData**](RelationshipCountMetaData.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.list_external_issue_response import ListExternalIssueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListExternalIssueResponse from a JSON string
list_external_issue_response_instance = ListExternalIssueResponse.from_json(json)
# print the JSON string representation of the object
print
ListExternalIssueResponse.to_json()

# convert the object into a dict
list_external_issue_response_dict = list_external_issue_response_instance.to_dict()
# create an instance of ListExternalIssueResponse from a dict
list_external_issue_response_form_dict = list_external_issue_response.from_dict(list_external_issue_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


