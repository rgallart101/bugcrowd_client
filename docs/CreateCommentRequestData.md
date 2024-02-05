# CreateCommentRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | [**CreateCommentRequestDataAttributes**](CreateCommentRequestDataAttributes.md) |  | 
**relationships** | [**CreateCommentRequestDataRelationships**](CreateCommentRequestDataRelationships.md) |  | 

## Example

```python
from bugcrowd_client.models.create_comment_request_data import CreateCommentRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCommentRequestData from a JSON string
create_comment_request_data_instance = CreateCommentRequestData.from_json(json)
# print the JSON string representation of the object
print
CreateCommentRequestData.to_json()

# convert the object into a dict
create_comment_request_data_dict = create_comment_request_data_instance.to_dict()
# create an instance of CreateCommentRequestData from a dict
create_comment_request_data_form_dict = create_comment_request_data.from_dict(create_comment_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


