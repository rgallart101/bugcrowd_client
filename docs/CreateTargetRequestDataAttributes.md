# CreateTargetRequestDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**category** | [**TargetTypeEnum**](TargetTypeEnum.md) |  | 

## Example

```python
from bugcrowd_client.models.create_target_request_data_attributes import CreateTargetRequestDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTargetRequestDataAttributes from a JSON string
create_target_request_data_attributes_instance = CreateTargetRequestDataAttributes.from_json(json)
# print the JSON string representation of the object
print
CreateTargetRequestDataAttributes.to_json()

# convert the object into a dict
create_target_request_data_attributes_dict = create_target_request_data_attributes_instance.to_dict()
# create an instance of CreateTargetRequestDataAttributes from a dict
create_target_request_data_attributes_form_dict = create_target_request_data_attributes.from_dict(
    create_target_request_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


