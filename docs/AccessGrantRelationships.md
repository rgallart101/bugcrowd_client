# AccessGrantRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grantee** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 
**resource** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.access_grant_relationships import AccessGrantRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of AccessGrantRelationships from a JSON string
access_grant_relationships_instance = AccessGrantRelationships.from_json(json)
# print the JSON string representation of the object
print
AccessGrantRelationships.to_json()

# convert the object into a dict
access_grant_relationships_dict = access_grant_relationships_instance.to_dict()
# create an instance of AccessGrantRelationships from a dict
access_grant_relationships_form_dict = access_grant_relationships.from_dict(access_grant_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


