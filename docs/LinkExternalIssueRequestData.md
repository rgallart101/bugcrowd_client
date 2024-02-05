# LinkExternalIssueRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | [**LinkExternalIssueRequestDataAttributes**](LinkExternalIssueRequestDataAttributes.md) |  | 
**relationships** | [**LinkExternalIssueRequestDataRelationships**](LinkExternalIssueRequestDataRelationships.md) |  | 

## Example

```python
from bugcrowd_client.models.link_external_issue_request_data import LinkExternalIssueRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of LinkExternalIssueRequestData from a JSON string
link_external_issue_request_data_instance = LinkExternalIssueRequestData.from_json(json)
# print the JSON string representation of the object
print
LinkExternalIssueRequestData.to_json()

# convert the object into a dict
link_external_issue_request_data_dict = link_external_issue_request_data_instance.to_dict()
# create an instance of LinkExternalIssueRequestData from a dict
link_external_issue_request_data_form_dict = link_external_issue_request_data.from_dict(
    link_external_issue_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


