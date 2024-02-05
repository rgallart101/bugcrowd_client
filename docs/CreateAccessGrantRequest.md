# CreateAccessGrantRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateAccessGrantRequestData**](CreateAccessGrantRequestData.md) |  | 

## Example

```python
from bugcrowd_client.models.create_access_grant_request import CreateAccessGrantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccessGrantRequest from a JSON string
create_access_grant_request_instance = CreateAccessGrantRequest.from_json(json)
# print the JSON string representation of the object
print
CreateAccessGrantRequest.to_json()

# convert the object into a dict
create_access_grant_request_dict = create_access_grant_request_instance.to_dict()
# create an instance of CreateAccessGrantRequest from a dict
create_access_grant_request_form_dict = create_access_grant_request.from_dict(create_access_grant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


