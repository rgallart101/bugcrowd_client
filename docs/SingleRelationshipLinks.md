# SingleRelationshipLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**related** | [**SingleRelationshipLinksRelated**](SingleRelationshipLinksRelated.md) |  | 

## Example

```python
from bugcrowd_client.models.single_relationship_links import SingleRelationshipLinks

# TODO update the JSON string below
json = "{}"
# create an instance of SingleRelationshipLinks from a JSON string
single_relationship_links_instance = SingleRelationshipLinks.from_json(json)
# print the JSON string representation of the object
print
SingleRelationshipLinks.to_json()

# convert the object into a dict
single_relationship_links_dict = single_relationship_links_instance.to_dict()
# create an instance of SingleRelationshipLinks from a dict
single_relationship_links_form_dict = single_relationship_links.from_dict(single_relationship_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


