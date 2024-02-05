# CreateTargetRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | [**CreateTargetRequestDataAttributes**](CreateTargetRequestDataAttributes.md) |  | 
**relationships** | [**CreateCustomerAssetRequestDataRelationships**](CreateCustomerAssetRequestDataRelationships.md) |  | 

## Example

```python
from bugcrowd_client.models.create_target_request_data import CreateTargetRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTargetRequestData from a JSON string
create_target_request_data_instance = CreateTargetRequestData.from_json(json)
# print the JSON string representation of the object
print
CreateTargetRequestData.to_json()

# convert the object into a dict
create_target_request_data_dict = create_target_request_data_instance.to_dict()
# create an instance of CreateTargetRequestData from a dict
create_target_request_data_form_dict = create_target_request_data.from_dict(create_target_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


