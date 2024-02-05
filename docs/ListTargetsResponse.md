# ListTargetsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Target]**](Target.md) |  | 
**included** | [**List[Organization]**](Organization.md) |  | [optional] 
**meta** | [**RelationshipCountMetaData**](RelationshipCountMetaData.md) |  | [optional] 
**links** | [**NavLinks**](NavLinks.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.list_targets_response import ListTargetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTargetsResponse from a JSON string
list_targets_response_instance = ListTargetsResponse.from_json(json)
# print the JSON string representation of the object
print
ListTargetsResponse.to_json()

# convert the object into a dict
list_targets_response_dict = list_targets_response_instance.to_dict()
# create an instance of ListTargetsResponse from a dict
list_targets_response_form_dict = list_targets_response.from_dict(list_targets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


