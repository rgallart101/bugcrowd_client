# CreateCommentRequestDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | 
**visibility_scope** | **str** |  | 

## Example

```python
from bugcrowd_client.models.create_comment_request_data_attributes import CreateCommentRequestDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCommentRequestDataAttributes from a JSON string
create_comment_request_data_attributes_instance = CreateCommentRequestDataAttributes.from_json(json)
# print the JSON string representation of the object
print
CreateCommentRequestDataAttributes.to_json()

# convert the object into a dict
create_comment_request_data_attributes_dict = create_comment_request_data_attributes_instance.to_dict()
# create an instance of CreateCommentRequestDataAttributes from a dict
create_comment_request_data_attributes_form_dict = create_comment_request_data_attributes.from_dict(
    create_comment_request_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


