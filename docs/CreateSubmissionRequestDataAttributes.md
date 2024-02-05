# CreateSubmissionRequestDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bug_url** | **str** |  | [optional] 
**custom_fields** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  | 
**extra_info** | **str** |  | [optional] 
**http_request** | **str** |  | [optional] 
**researcher_email** | **str** |  | [optional] 
**severity** | **int** |  | [optional] 
**state** | [**SubstateEnum**](SubstateEnum.md) |  | [optional] 
**submitted_at** | **datetime** |  | [optional] 
**title** | **str** |  | 
**cvss_string** | **str** |  | [optional] 
**vrt_id** | **str** |  | [optional] 

## Example

```python
from bugcrowd_client.models.create_submission_request_data_attributes import CreateSubmissionRequestDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubmissionRequestDataAttributes from a JSON string
create_submission_request_data_attributes_instance = CreateSubmissionRequestDataAttributes.from_json(json)
# print the JSON string representation of the object
print
CreateSubmissionRequestDataAttributes.to_json()

# convert the object into a dict
create_submission_request_data_attributes_dict = create_submission_request_data_attributes_instance.to_dict()
# create an instance of CreateSubmissionRequestDataAttributes from a dict
create_submission_request_data_attributes_form_dict = create_submission_request_data_attributes.from_dict(
    create_submission_request_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


