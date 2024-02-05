# ManyRelationshipLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**related** | [**ManyRelationshipLinksRelated**](ManyRelationshipLinksRelated.md) |  | 

## Example

```python
from bugcrowd_client.models.many_relationship_links import ManyRelationshipLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ManyRelationshipLinks from a JSON string
many_relationship_links_instance = ManyRelationshipLinks.from_json(json)
# print the JSON string representation of the object
print
ManyRelationshipLinks.to_json()

# convert the object into a dict
many_relationship_links_dict = many_relationship_links_instance.to_dict()
# create an instance of ManyRelationshipLinks from a dict
many_relationship_links_form_dict = many_relationship_links.from_dict(many_relationship_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


