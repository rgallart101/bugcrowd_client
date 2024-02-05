# CreateCommentRequestDataRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**submission** | [**CreateCommentRequestDataRelationshipsSubmission**](CreateCommentRequestDataRelationshipsSubmission.md) |  | 

## Example

```python
from bugcrowd_client.models.create_comment_request_data_relationships import CreateCommentRequestDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCommentRequestDataRelationships from a JSON string
create_comment_request_data_relationships_instance = CreateCommentRequestDataRelationships.from_json(json)
# print the JSON string representation of the object
print
CreateCommentRequestDataRelationships.to_json()

# convert the object into a dict
create_comment_request_data_relationships_dict = create_comment_request_data_relationships_instance.to_dict()
# create an instance of CreateCommentRequestDataRelationships from a dict
create_comment_request_data_relationships_form_dict = create_comment_request_data_relationships.from_dict(
    create_comment_request_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


