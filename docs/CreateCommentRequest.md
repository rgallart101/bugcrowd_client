# CreateCommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateCommentRequestData**](CreateCommentRequestData.md) |  | 

## Example

```python
from bugcrowd_client.models.create_comment_request import CreateCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCommentRequest from a JSON string
create_comment_request_instance = CreateCommentRequest.from_json(json)
# print the JSON string representation of the object
print
CreateCommentRequest.to_json()

# convert the object into a dict
create_comment_request_dict = create_comment_request_instance.to_dict()
# create an instance of CreateCommentRequest from a dict
create_comment_request_form_dict = create_comment_request.from_dict(create_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


