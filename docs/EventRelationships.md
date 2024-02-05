# EventRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor** | [**EventRelationshipsActor**](EventRelationshipsActor.md) |  | 
**resource** | [**EventRelationshipsResource**](EventRelationshipsResource.md) |  | 

## Example

```python
from bugcrowd_client.models.event_relationships import EventRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of EventRelationships from a JSON string
event_relationships_instance = EventRelationships.from_json(json)
# print the JSON string representation of the object
print
EventRelationships.to_json()

# convert the object into a dict
event_relationships_dict = event_relationships_instance.to_dict()
# create an instance of EventRelationships from a dict
event_relationships_form_dict = event_relationships.from_dict(event_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


