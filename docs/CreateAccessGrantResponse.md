# CreateAccessGrantResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AccessGrant**](AccessGrant.md) |  | 

## Example

```python
from bugcrowd_client.models.create_access_grant_response import CreateAccessGrantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccessGrantResponse from a JSON string
create_access_grant_response_instance = CreateAccessGrantResponse.from_json(json)
# print the JSON string representation of the object
print
CreateAccessGrantResponse.to_json()

# convert the object into a dict
create_access_grant_response_dict = create_access_grant_response_instance.to_dict()
# create an instance of CreateAccessGrantResponse from a dict
create_access_grant_response_form_dict = create_access_grant_response.from_dict(create_access_grant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


