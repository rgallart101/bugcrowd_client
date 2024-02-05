# LinkExternalIssueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LinkExternalIssueRequestData**](LinkExternalIssueRequestData.md) |  | 

## Example

```python
from bugcrowd_client.models.link_external_issue_request import LinkExternalIssueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LinkExternalIssueRequest from a JSON string
link_external_issue_request_instance = LinkExternalIssueRequest.from_json(json)
# print the JSON string representation of the object
print
LinkExternalIssueRequest.to_json()

# convert the object into a dict
link_external_issue_request_dict = link_external_issue_request_instance.to_dict()
# create an instance of LinkExternalIssueRequest from a dict
link_external_issue_request_form_dict = link_external_issue_request.from_dict(link_external_issue_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


