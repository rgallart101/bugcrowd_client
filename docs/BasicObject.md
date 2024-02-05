# BasicObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 

## Example

```python
from bugcrowd_client.models.basic_object import BasicObject

# TODO update the JSON string below
json = "{}"
# create an instance of BasicObject from a JSON string
basic_object_instance = BasicObject.from_json(json)
# print the JSON string representation of the object
print
BasicObject.to_json()

# convert the object into a dict
basic_object_dict = basic_object_instance.to_dict()
# create an instance of BasicObject from a dict
basic_object_form_dict = basic_object.from_dict(basic_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


