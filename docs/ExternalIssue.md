# ExternalIssue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 
**attributes** | [**ExternalIssueAttributes**](ExternalIssueAttributes.md) |  | [optional] 
**relationships** | [**ExternalIssueRelationships**](ExternalIssueRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.external_issue import ExternalIssue

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalIssue from a JSON string
external_issue_instance = ExternalIssue.from_json(json)
# print the JSON string representation of the object
print
ExternalIssue.to_json()

# convert the object into a dict
external_issue_dict = external_issue_instance.to_dict()
# create an instance of ExternalIssue from a dict
external_issue_form_dict = external_issue.from_dict(external_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


