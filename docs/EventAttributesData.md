# EventAttributesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocked_by** | **str** |  | 
**source** | **str** |  | [optional] 
**current_substate** | **str** |  | [optional] 
**changes** | [**EventDataSubmissionUpdatedChanges**](EventDataSubmissionUpdatedChanges.md) |  | 
**duplicate_ids** | **List[str]** |  | 

## Example

```python
from bugcrowd_client.models.event_attributes_data import EventAttributesData

# TODO update the JSON string below
json = "{}"
# create an instance of EventAttributesData from a JSON string
event_attributes_data_instance = EventAttributesData.from_json(json)
# print the JSON string representation of the object
print
EventAttributesData.to_json()

# convert the object into a dict
event_attributes_data_dict = event_attributes_data_instance.to_dict()
# create an instance of EventAttributesData from a dict
event_attributes_data_form_dict = event_attributes_data.from_dict(event_attributes_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


