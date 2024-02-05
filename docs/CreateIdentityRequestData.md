# CreateIdentityRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | [**CreateIdentityRequestDataAttributes**](CreateIdentityRequestDataAttributes.md) |  | 

## Example

```python
from bugcrowd_client.models.create_identity_request_data import CreateIdentityRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIdentityRequestData from a JSON string
create_identity_request_data_instance = CreateIdentityRequestData.from_json(json)
# print the JSON string representation of the object
print
CreateIdentityRequestData.to_json()

# convert the object into a dict
create_identity_request_data_dict = create_identity_request_data_instance.to_dict()
# create an instance of CreateIdentityRequestData from a dict
create_identity_request_data_form_dict = create_identity_request_data.from_dict(create_identity_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


