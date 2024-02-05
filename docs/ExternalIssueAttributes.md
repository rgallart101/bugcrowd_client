# ExternalIssueAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_id** | **str** | The identifier for the external issue | [optional] 
**remote_url** | **object** | URL of the external issue | [optional] 

## Example

```python
from bugcrowd_client.models.external_issue_attributes import ExternalIssueAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalIssueAttributes from a JSON string
external_issue_attributes_instance = ExternalIssueAttributes.from_json(json)
# print the JSON string representation of the object
print
ExternalIssueAttributes.to_json()

# convert the object into a dict
external_issue_attributes_dict = external_issue_attributes_instance.to_dict()
# create an instance of ExternalIssueAttributes from a dict
external_issue_attributes_form_dict = external_issue_attributes.from_dict(external_issue_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


