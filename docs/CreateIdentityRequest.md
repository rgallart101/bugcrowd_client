# CreateIdentityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateIdentityRequestData**](CreateIdentityRequestData.md) |  | 

## Example

```python
from bugcrowd_client.models.create_identity_request import CreateIdentityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIdentityRequest from a JSON string
create_identity_request_instance = CreateIdentityRequest.from_json(json)
# print the JSON string representation of the object
print
CreateIdentityRequest.to_json()

# convert the object into a dict
create_identity_request_dict = create_identity_request_instance.to_dict()
# create an instance of CreateIdentityRequest from a dict
create_identity_request_form_dict = create_identity_request.from_dict(create_identity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


