# CreateSubmissionRequestDataRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program** | [**ProgramNotNullable**](ProgramNotNullable.md) |  | 
**target** | [**TargetNotNullable**](TargetNotNullable.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.create_submission_request_data_relationships import CreateSubmissionRequestDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubmissionRequestDataRelationships from a JSON string
create_submission_request_data_relationships_instance = CreateSubmissionRequestDataRelationships.from_json(json)
# print the JSON string representation of the object
print
CreateSubmissionRequestDataRelationships.to_json()

# convert the object into a dict
create_submission_request_data_relationships_dict = create_submission_request_data_relationships_instance.to_dict()
# create an instance of CreateSubmissionRequestDataRelationships from a dict
create_submission_request_data_relationships_form_dict = create_submission_request_data_relationships.from_dict(
    create_submission_request_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


