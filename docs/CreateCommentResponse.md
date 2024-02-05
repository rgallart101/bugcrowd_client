# CreateCommentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Comment**](Comment.md) |  | 

## Example

```python
from bugcrowd_client.models.create_comment_response import CreateCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCommentResponse from a JSON string
create_comment_response_instance = CreateCommentResponse.from_json(json)
# print the JSON string representation of the object
print
CreateCommentResponse.to_json()

# convert the object into a dict
create_comment_response_dict = create_comment_response_instance.to_dict()
# create an instance of CreateCommentResponse from a dict
create_comment_response_form_dict = create_comment_response.from_dict(create_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


