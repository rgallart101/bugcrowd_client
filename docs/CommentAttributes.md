# CommentAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The contents of the comment | [optional] 
**created_at** | **str** | Time at which the object was created | [optional] 
**visibility_scope** | **str** | Which parties this comment can be seen by | [optional] 

## Example

```python
from bugcrowd_client.models.comment_attributes import CommentAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CommentAttributes from a JSON string
comment_attributes_instance = CommentAttributes.from_json(json)
# print the JSON string representation of the object
print
CommentAttributes.to_json()

# convert the object into a dict
comment_attributes_dict = comment_attributes_instance.to_dict()
# create an instance of CommentAttributes from a dict
comment_attributes_form_dict = comment_attributes.from_dict(comment_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


