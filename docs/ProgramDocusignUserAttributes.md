# ProgramDocusignUserAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the program docusign user | [optional] 
**status** | **str** | Status of the program docusign user | [optional] 
**approved_at** | **datetime** | Time at which the program docusign user was approved | [optional] 
**last_signed_at** | **datetime** | Time at which the program docusign user last signed | [optional] 

## Example

```python
from bugcrowd_client.models.program_docusign_user_attributes import ProgramDocusignUserAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramDocusignUserAttributes from a JSON string
program_docusign_user_attributes_instance = ProgramDocusignUserAttributes.from_json(json)
# print the JSON string representation of the object
print
ProgramDocusignUserAttributes.to_json()

# convert the object into a dict
program_docusign_user_attributes_dict = program_docusign_user_attributes_instance.to_dict()
# create an instance of ProgramDocusignUserAttributes from a dict
program_docusign_user_attributes_form_dict = program_docusign_user_attributes.from_dict(
    program_docusign_user_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


