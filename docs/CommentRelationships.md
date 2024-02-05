# CommentRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 
**file_attachments** | [**ManyRelationship**](ManyRelationship.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.comment_relationships import CommentRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of CommentRelationships from a JSON string
comment_relationships_instance = CommentRelationships.from_json(json)
# print the JSON string representation of the object
print
CommentRelationships.to_json()

# convert the object into a dict
comment_relationships_dict = comment_relationships_instance.to_dict()
# create an instance of CommentRelationships from a dict
comment_relationships_form_dict = comment_relationships.from_dict(comment_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


