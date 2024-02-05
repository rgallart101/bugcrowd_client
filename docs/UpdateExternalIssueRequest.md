# UpdateExternalIssueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UpdateExternalIssueRequestData**](UpdateExternalIssueRequestData.md) |  | 

## Example

```python
from bugcrowd_client.models.update_external_issue_request import UpdateExternalIssueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateExternalIssueRequest from a JSON string
update_external_issue_request_instance = UpdateExternalIssueRequest.from_json(json)
# print the JSON string representation of the object
print
UpdateExternalIssueRequest.to_json()

# convert the object into a dict
update_external_issue_request_dict = update_external_issue_request_instance.to_dict()
# create an instance of UpdateExternalIssueRequest from a dict
update_external_issue_request_form_dict = update_external_issue_request.from_dict(update_external_issue_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


