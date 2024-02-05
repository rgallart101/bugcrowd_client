# UserRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**ManyRelationship**](ManyRelationship.md) |  | [optional] 
**program_docusign_users** | [**ManyRelationship**](ManyRelationship.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.user_relationships import UserRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of UserRelationships from a JSON string
user_relationships_instance = UserRelationships.from_json(json)
# print the JSON string representation of the object
print
UserRelationships.to_json()

# convert the object into a dict
user_relationships_dict = user_relationships_instance.to_dict()
# create an instance of UserRelationships from a dict
user_relationships_form_dict = user_relationships.from_dict(user_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


