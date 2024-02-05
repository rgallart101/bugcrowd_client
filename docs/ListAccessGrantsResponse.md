# ListAccessGrantsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AccessGrant]**](AccessGrant.md) |  | 
**included** | [**List[AccessGrantIncludedResponseInner]**](AccessGrantIncludedResponseInner.md) |  | [optional] 
**meta** | [**RelationshipCountMetaData**](RelationshipCountMetaData.md) |  | [optional] 
**links** | [**NavLinks**](NavLinks.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.list_access_grants_response import ListAccessGrantsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAccessGrantsResponse from a JSON string
list_access_grants_response_instance = ListAccessGrantsResponse.from_json(json)
# print the JSON string representation of the object
print
ListAccessGrantsResponse.to_json()

# convert the object into a dict
list_access_grants_response_dict = list_access_grants_response_instance.to_dict()
# create an instance of ListAccessGrantsResponse from a dict
list_access_grants_response_form_dict = list_access_grants_response.from_dict(list_access_grants_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


