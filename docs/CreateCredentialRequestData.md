# CreateCredentialRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | **object** |  | 
**relationships** | [**CreateCredentialRequestDataRelationships**](CreateCredentialRequestDataRelationships.md) |  | 

## Example

```python
from bugcrowd_client.models.create_credential_request_data import CreateCredentialRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCredentialRequestData from a JSON string
create_credential_request_data_instance = CreateCredentialRequestData.from_json(json)
# print the JSON string representation of the object
print
CreateCredentialRequestData.to_json()

# convert the object into a dict
create_credential_request_data_dict = create_credential_request_data_instance.to_dict()
# create an instance of CreateCredentialRequestData from a dict
create_credential_request_data_form_dict = create_credential_request_data.from_dict(create_credential_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


