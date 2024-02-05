# UpdateExternalIssueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ExternalIssue**](ExternalIssue.md) |  | 

## Example

```python
from bugcrowd_client.models.update_external_issue_response import UpdateExternalIssueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateExternalIssueResponse from a JSON string
update_external_issue_response_instance = UpdateExternalIssueResponse.from_json(json)
# print the JSON string representation of the object
print
UpdateExternalIssueResponse.to_json()

# convert the object into a dict
update_external_issue_response_dict = update_external_issue_response_instance.to_dict()
# create an instance of UpdateExternalIssueResponse from a dict
update_external_issue_response_form_dict = update_external_issue_response.from_dict(update_external_issue_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


