# LinkExternalIssueRequestDataRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**SubmissionNullable**](SubmissionNullable.md) |  | 
**integration** | [**LinkExternalIssueRequestDataRelationshipsIntegration**](LinkExternalIssueRequestDataRelationshipsIntegration.md) |  | 

## Example

```python
from bugcrowd_client.models.link_external_issue_request_data_relationships import
    LinkExternalIssueRequestDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of LinkExternalIssueRequestDataRelationships from a JSON string
link_external_issue_request_data_relationships_instance = LinkExternalIssueRequestDataRelationships.from_json(json)
# print the JSON string representation of the object
print
LinkExternalIssueRequestDataRelationships.to_json()

# convert the object into a dict
link_external_issue_request_data_relationships_dict = link_external_issue_request_data_relationships_instance.to_dict()
# create an instance of LinkExternalIssueRequestDataRelationships from a dict
link_external_issue_request_data_relationships_form_dict = link_external_issue_request_data_relationships.from_dict(
    link_external_issue_request_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


