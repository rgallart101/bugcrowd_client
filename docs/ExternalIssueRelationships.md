# ExternalIssueRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 
**resource** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.external_issue_relationships import ExternalIssueRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalIssueRelationships from a JSON string
external_issue_relationships_instance = ExternalIssueRelationships.from_json(json)
# print the JSON string representation of the object
print
ExternalIssueRelationships.to_json()

# convert the object into a dict
external_issue_relationships_dict = external_issue_relationships_instance.to_dict()
# create an instance of ExternalIssueRelationships from a dict
external_issue_relationships_form_dict = external_issue_relationships.from_dict(external_issue_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


