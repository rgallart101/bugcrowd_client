# ProgramBriefAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinated_disclosure** | **bool** | Indicates whether the program allows researchers to request to disclose submissions | [optional] 
**created_at** | **str** | Time at which the object was created | [optional] 
**demo** | **bool** | Indicates whether the program is set to demo mode, usually true before a program goes live | [optional] 
**description** | **str** | Details about the goal of your bounty program | [optional] 
**tagline** | **str** | Short sentence that concisely describes your company, product, or bounty program | [optional] 
**rewards_overview** | **str** | Whether compensation is provided for (valid and unique) issues, and the form and magnitude of that compensation | [optional] 
**targets_overview** | **str** | Customer-defined explanation of the targets defined in the program | [optional] 

## Example

```python
from bugcrowd_client.models.program_brief_attributes import ProgramBriefAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramBriefAttributes from a JSON string
program_brief_attributes_instance = ProgramBriefAttributes.from_json(json)
# print the JSON string representation of the object
print
ProgramBriefAttributes.to_json()

# convert the object into a dict
program_brief_attributes_dict = program_brief_attributes_instance.to_dict()
# create an instance of ProgramBriefAttributes from a dict
program_brief_attributes_form_dict = program_brief_attributes.from_dict(program_brief_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


