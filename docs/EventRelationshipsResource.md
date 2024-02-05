# EventRelationshipsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EventRelationshipsResourceData**](EventRelationshipsResourceData.md) |  | 

## Example

```python
from bugcrowd_client.models.event_relationships_resource import EventRelationshipsResource

# TODO update the JSON string below
json = "{}"
# create an instance of EventRelationshipsResource from a JSON string
event_relationships_resource_instance = EventRelationshipsResource.from_json(json)
# print the JSON string representation of the object
print
EventRelationshipsResource.to_json()

# convert the object into a dict
event_relationships_resource_dict = event_relationships_resource_instance.to_dict()
# create an instance of EventRelationshipsResource from a dict
event_relationships_resource_form_dict = event_relationships_resource.from_dict(event_relationships_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


