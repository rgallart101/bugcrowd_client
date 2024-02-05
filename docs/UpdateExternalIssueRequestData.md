# UpdateExternalIssueRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | [**LinkExternalIssueRequestDataAttributes**](LinkExternalIssueRequestDataAttributes.md) |  | 

## Example

```python
from bugcrowd_client.models.update_external_issue_request_data import UpdateExternalIssueRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateExternalIssueRequestData from a JSON string
update_external_issue_request_data_instance = UpdateExternalIssueRequestData.from_json(json)
# print the JSON string representation of the object
print
UpdateExternalIssueRequestData.to_json()

# convert the object into a dict
update_external_issue_request_data_dict = update_external_issue_request_data_instance.to_dict()
# create an instance of UpdateExternalIssueRequestData from a dict
update_external_issue_request_data_form_dict = update_external_issue_request_data.from_dict(
    update_external_issue_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


