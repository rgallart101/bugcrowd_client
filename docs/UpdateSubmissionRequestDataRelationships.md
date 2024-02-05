# UpdateSubmissionRequestDataRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee** | [**IdentityNullable**](IdentityNullable.md) |  | [optional] 
**cvss_vector** | [**CvssVectorNotNullable**](CvssVectorNotNullable.md) |  | [optional] 
**duplicate_of** | [**SubmissionNullable**](SubmissionNullable.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.update_submission_request_data_relationships import UpdateSubmissionRequestDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubmissionRequestDataRelationships from a JSON string
update_submission_request_data_relationships_instance = UpdateSubmissionRequestDataRelationships.from_json(json)
# print the JSON string representation of the object
print
UpdateSubmissionRequestDataRelationships.to_json()

# convert the object into a dict
update_submission_request_data_relationships_dict = update_submission_request_data_relationships_instance.to_dict()
# create an instance of UpdateSubmissionRequestDataRelationships from a dict
update_submission_request_data_relationships_form_dict = update_submission_request_data_relationships.from_dict(
    update_submission_request_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


