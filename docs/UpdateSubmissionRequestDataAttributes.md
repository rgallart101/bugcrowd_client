# UpdateSubmissionRequestDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bug_url** | **str** |  | [optional] 
**custom_fields** | **Dict[str, str]** |  | [optional] 
**http_request** | **str** |  | [optional] 
**remediation_advice** | **str** |  | [optional] 
**severity** | **int** |  | [optional] 
**state** | [**SubstateEnum**](SubstateEnum.md) |  | [optional] 
**title** | **str** |  | [optional] 
**vrt_id** | **str** |  | [optional] 
**vulnerability_references** | **str** |  | [optional] 

## Example

```python
from bugcrowd_client.models.update_submission_request_data_attributes import UpdateSubmissionRequestDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubmissionRequestDataAttributes from a JSON string
update_submission_request_data_attributes_instance = UpdateSubmissionRequestDataAttributes.from_json(json)
# print the JSON string representation of the object
print
UpdateSubmissionRequestDataAttributes.to_json()

# convert the object into a dict
update_submission_request_data_attributes_dict = update_submission_request_data_attributes_instance.to_dict()
# create an instance of UpdateSubmissionRequestDataAttributes from a dict
update_submission_request_data_attributes_form_dict = update_submission_request_data_attributes.from_dict(
    update_submission_request_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


