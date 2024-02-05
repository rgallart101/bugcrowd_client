# ProgramIncludedResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 
**attributes** | [**SubmissionAttributes**](SubmissionAttributes.md) |  | [optional] 
**relationships** | [**SubmissionRelationships**](SubmissionRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.program_included_response_inner import ProgramIncludedResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramIncludedResponseInner from a JSON string
program_included_response_inner_instance = ProgramIncludedResponseInner.from_json(json)
# print the JSON string representation of the object
print
ProgramIncludedResponseInner.to_json()

# convert the object into a dict
program_included_response_inner_dict = program_included_response_inner_instance.to_dict()
# create an instance of ProgramIncludedResponseInner from a dict
program_included_response_inner_form_dict = program_included_response_inner.from_dict(
    program_included_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


