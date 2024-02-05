# TargetAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Target Name (URL/Location) | [optional] 
**category** | **str** | Categorizes the target. Categories include website, API, IOS, Android, IOT, hardware, and other. | [optional] 

## Example

```python
from bugcrowd_client.models.target_attributes import TargetAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of TargetAttributes from a JSON string
target_attributes_instance = TargetAttributes.from_json(json)
# print the JSON string representation of the object
print
TargetAttributes.to_json()

# convert the object into a dict
target_attributes_dict = target_attributes_instance.to_dict()
# create an instance of TargetAttributes from a dict
target_attributes_form_dict = target_attributes.from_dict(target_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


