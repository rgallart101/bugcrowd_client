# UpdateSubmissionRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | [**UpdateSubmissionRequestDataAttributes**](UpdateSubmissionRequestDataAttributes.md) |  | [optional] 
**relationships** | [**UpdateSubmissionRequestDataRelationships**](UpdateSubmissionRequestDataRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.update_submission_request_data import UpdateSubmissionRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubmissionRequestData from a JSON string
update_submission_request_data_instance = UpdateSubmissionRequestData.from_json(json)
# print the JSON string representation of the object
print
UpdateSubmissionRequestData.to_json()

# convert the object into a dict
update_submission_request_data_dict = update_submission_request_data_instance.to_dict()
# create an instance of UpdateSubmissionRequestData from a dict
update_submission_request_data_form_dict = update_submission_request_data.from_dict(update_submission_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


