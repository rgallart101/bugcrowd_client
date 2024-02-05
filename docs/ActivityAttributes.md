# ActivityAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | Timestamp of when the activity was created | [optional] 
**key** | **str** | Event key unique to the source of the activity | [optional] 

## Example

```python
from bugcrowd_client.models.activity_attributes import ActivityAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityAttributes from a JSON string
activity_attributes_instance = ActivityAttributes.from_json(json)
# print the JSON string representation of the object
print
ActivityAttributes.to_json()

# convert the object into a dict
activity_attributes_dict = activity_attributes_instance.to_dict()
# create an instance of ActivityAttributes from a dict
activity_attributes_form_dict = activity_attributes.from_dict(activity_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


