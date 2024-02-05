# ManyRelationshipLinksRelated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | 
**meta** | [**RelationshipCountMetaData**](RelationshipCountMetaData.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.many_relationship_links_related import ManyRelationshipLinksRelated

# TODO update the JSON string below
json = "{}"
# create an instance of ManyRelationshipLinksRelated from a JSON string
many_relationship_links_related_instance = ManyRelationshipLinksRelated.from_json(json)
# print the JSON string representation of the object
print
ManyRelationshipLinksRelated.to_json()

# convert the object into a dict
many_relationship_links_related_dict = many_relationship_links_related_instance.to_dict()
# create an instance of ManyRelationshipLinksRelated from a dict
many_relationship_links_related_form_dict = many_relationship_links_related.from_dict(
    many_relationship_links_related_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


