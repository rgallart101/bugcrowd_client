# SubmissionIncludedResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | 
**attributes** | [**TargetAttributes**](TargetAttributes.md) |  | [optional] 
**relationships** | [**TargetRelationships**](TargetRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.submission_included_response_inner import SubmissionIncludedResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionIncludedResponseInner from a JSON string
submission_included_response_inner_instance = SubmissionIncludedResponseInner.from_json(json)
# print the JSON string representation of the object
print
SubmissionIncludedResponseInner.to_json()

# convert the object into a dict
submission_included_response_inner_dict = submission_included_response_inner_instance.to_dict()
# create an instance of SubmissionIncludedResponseInner from a dict
submission_included_response_inner_form_dict = submission_included_response_inner.from_dict(
    submission_included_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


