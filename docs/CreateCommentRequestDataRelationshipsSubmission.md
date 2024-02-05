# CreateCommentRequestDataRelationshipsSubmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateCommentRequestDataRelationshipsSubmissionData**](CreateCommentRequestDataRelationshipsSubmissionData.md) |  | 

## Example

```python
from bugcrowd_client.models.create_comment_request_data_relationships_submission import
    CreateCommentRequestDataRelationshipsSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCommentRequestDataRelationshipsSubmission from a JSON string
create_comment_request_data_relationships_submission_instance = CreateCommentRequestDataRelationshipsSubmission.from_json(
    json)
# print the JSON string representation of the object
print
CreateCommentRequestDataRelationshipsSubmission.to_json()

# convert the object into a dict
create_comment_request_data_relationships_submission_dict = create_comment_request_data_relationships_submission_instance.to_dict()
# create an instance of CreateCommentRequestDataRelationshipsSubmission from a dict
create_comment_request_data_relationships_submission_form_dict = create_comment_request_data_relationships_submission.from_dict(
    create_comment_request_data_relationships_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


