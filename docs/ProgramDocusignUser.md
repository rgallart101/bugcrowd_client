# ProgramDocusignUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 
**attributes** | [**ProgramDocusignUserAttributes**](ProgramDocusignUserAttributes.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.program_docusign_user import ProgramDocusignUser

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramDocusignUser from a JSON string
program_docusign_user_instance = ProgramDocusignUser.from_json(json)
# print the JSON string representation of the object
print
ProgramDocusignUser.to_json()

# convert the object into a dict
program_docusign_user_dict = program_docusign_user_instance.to_dict()
# create an instance of ProgramDocusignUser from a dict
program_docusign_user_form_dict = program_docusign_user.from_dict(program_docusign_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


