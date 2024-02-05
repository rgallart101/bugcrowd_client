# SubmissionAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bug_url** | **str** | URL / Location of vulnerability (optional)  _This field is only available with direct access to the submission&#39;s program_  | [optional] 
**custom_fields** | **Dict[str, str]** | Internal metadata associated with submissions. Can be configured in the UI  _This field is only available with direct access to the submission&#39;s program_  | [optional] 
**description** | **str** | Describes the vulnerability, the steps to reproduce or proof-of-concept, and its impact  _This field is only available with direct access to the submission&#39;s program_  | [optional] 
**duplicate** | **bool** | Indicates that this submission is a duplicate of another submission | [optional] 
**extra_info** | **str** | Additional information (optional)  _This field is only available with direct access to the submission&#39;s program_  | [optional] 
**http_request** | **str** | Trace dump / HTTP request (optional)  _This field is only available with direct access to the submission&#39;s program_  | [optional] 
**last_transitioned_to_informational_at** | **datetime** |  | [optional] 
**last_transitioned_to_not_applicable_at** | **datetime** |  | [optional] 
**last_transitioned_to_not_reproducible_at** | **datetime** |  | [optional] 
**last_transitioned_to_out_of_scope_at** | **datetime** |  | [optional] 
**last_transitioned_to_resolved_at** | **datetime** |  | [optional] 
**last_transitioned_to_triaged_at** | **datetime** |  | [optional] 
**last_transitioned_to_unresolved_at** | **datetime** |  | [optional] 
**severity** | **int** |  | [optional] 
**remediation_advice** | **str** | Supplied by Bugcrowd&#39;s VRT, if enabled remediation advice can give hints to help address vulnerabilities associated with specific submissions  _This field is only available with direct access to the submission&#39;s program_  | [optional] 
**submitted_at** | **datetime** | Timestamp indicating when the submission was submitted | [optional] 
**source** | [**SourceEnum**](SourceEnum.md) |  | [optional] 
**state** | [**SubstateEnum**](SubstateEnum.md) |  | [optional] 
**title** | **str** | The title of the submission.  _This field is only available with direct access to the submission&#39;s program. Without direct access the title will read as &#39;Original submission in another program&#39;._  | [optional] 
**vrt_id** | **str** |  | [optional] 
**vrt_version** | **str** |  | [optional] 
**vulnerability_references** | **str** | External links to references about the vrt_id related to the submission. Can be edited to custom references not defined in the VRT.  _This field is only available with direct access to the submission&#39;s program_  | [optional] 

## Example

```python
from bugcrowd_client.models.submission_attributes import SubmissionAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionAttributes from a JSON string
submission_attributes_instance = SubmissionAttributes.from_json(json)
# print the JSON string representation of the object
print
SubmissionAttributes.to_json()

# convert the object into a dict
submission_attributes_dict = submission_attributes_instance.to_dict()
# create an instance of SubmissionAttributes from a dict
submission_attributes_form_dict = submission_attributes.from_dict(submission_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


