# CreateSubmissionRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | [**CreateSubmissionRequestDataAttributes**](CreateSubmissionRequestDataAttributes.md) |  | 
**relationships** | [**CreateSubmissionRequestDataRelationships**](CreateSubmissionRequestDataRelationships.md) |  | 

## Example

```python
from bugcrowd_client.models.create_submission_request_data import CreateSubmissionRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubmissionRequestData from a JSON string
create_submission_request_data_instance = CreateSubmissionRequestData.from_json(json)
# print the JSON string representation of the object
print
CreateSubmissionRequestData.to_json()

# convert the object into a dict
create_submission_request_data_dict = create_submission_request_data_instance.to_dict()
# create an instance of CreateSubmissionRequestData from a dict
create_submission_request_data_form_dict = create_submission_request_data.from_dict(create_submission_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


