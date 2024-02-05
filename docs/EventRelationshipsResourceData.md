# EventRelationshipsResourceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | Unique identifier for the resource | 

## Example

```python
from bugcrowd_client.models.event_relationships_resource_data import EventRelationshipsResourceData

# TODO update the JSON string below
json = "{}"
# create an instance of EventRelationshipsResourceData from a JSON string
event_relationships_resource_data_instance = EventRelationshipsResourceData.from_json(json)
# print the JSON string representation of the object
print
EventRelationshipsResourceData.to_json()

# convert the object into a dict
event_relationships_resource_data_dict = event_relationships_resource_data_instance.to_dict()
# create an instance of EventRelationshipsResourceData from a dict
event_relationships_resource_data_form_dict = event_relationships_resource_data.from_dict(
    event_relationships_resource_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


