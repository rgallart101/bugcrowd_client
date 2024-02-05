# EventAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**key** | **str** |  | [optional] 
**data** | [**EventAttributesData**](EventAttributesData.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.event_attributes import EventAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of EventAttributes from a JSON string
event_attributes_instance = EventAttributes.from_json(json)
# print the JSON string representation of the object
print
EventAttributes.to_json()

# convert the object into a dict
event_attributes_dict = event_attributes_instance.to_dict()
# create an instance of EventAttributes from a dict
event_attributes_form_dict = event_attributes.from_dict(event_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


