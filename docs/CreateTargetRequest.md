# CreateTargetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateTargetRequestData**](CreateTargetRequestData.md) |  | 

## Example

```python
from bugcrowd_client.models.create_target_request import CreateTargetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTargetRequest from a JSON string
create_target_request_instance = CreateTargetRequest.from_json(json)
# print the JSON string representation of the object
print
CreateTargetRequest.to_json()

# convert the object into a dict
create_target_request_dict = create_target_request_instance.to_dict()
# create an instance of CreateTargetRequest from a dict
create_target_request_form_dict = create_target_request.from_dict(create_target_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


