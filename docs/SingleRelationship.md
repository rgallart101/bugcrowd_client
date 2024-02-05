# SingleRelationship


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**SingleRelationshipLinks**](SingleRelationshipLinks.md) |  | 
**data** | [**BasicObject**](BasicObject.md) |  | 

## Example

```python
from bugcrowd_client.models.single_relationship import SingleRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of SingleRelationship from a JSON string
single_relationship_instance = SingleRelationship.from_json(json)
# print the JSON string representation of the object
print
SingleRelationship.to_json()

# convert the object into a dict
single_relationship_dict = single_relationship_instance.to_dict()
# create an instance of SingleRelationship from a dict
single_relationship_form_dict = single_relationship.from_dict(single_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


