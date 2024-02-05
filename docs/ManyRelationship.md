# ManyRelationship


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ManyRelationshipLinks**](ManyRelationshipLinks.md) |  | 
**data** | [**List[BasicObject]**](BasicObject.md) |  | 

## Example

```python
from bugcrowd_client.models.many_relationship import ManyRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of ManyRelationship from a JSON string
many_relationship_instance = ManyRelationship.from_json(json)
# print the JSON string representation of the object
print
ManyRelationship.to_json()

# convert the object into a dict
many_relationship_dict = many_relationship_instance.to_dict()
# create an instance of ManyRelationship from a dict
many_relationship_form_dict = many_relationship.from_dict(many_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


