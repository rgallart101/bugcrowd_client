# LinkExternalIssueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ExternalIssue**](ExternalIssue.md) |  | 
**included** | [**List[Submission]**](Submission.md) |  | [optional] 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.link_external_issue_response import LinkExternalIssueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LinkExternalIssueResponse from a JSON string
link_external_issue_response_instance = LinkExternalIssueResponse.from_json(json)
# print the JSON string representation of the object
print
LinkExternalIssueResponse.to_json()

# convert the object into a dict
link_external_issue_response_dict = link_external_issue_response_instance.to_dict()
# create an instance of LinkExternalIssueResponse from a dict
link_external_issue_response_form_dict = link_external_issue_response.from_dict(link_external_issue_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


