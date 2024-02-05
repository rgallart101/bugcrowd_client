# CreateSubmissionResponseIncludedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 
**attributes** | [**ClaimTicketAttributes**](ClaimTicketAttributes.md) |  | [optional] 
**relationships** | [**ClaimTicketRelationships**](ClaimTicketRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.create_submission_response_included_inner import CreateSubmissionResponseIncludedInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubmissionResponseIncludedInner from a JSON string
create_submission_response_included_inner_instance = CreateSubmissionResponseIncludedInner.from_json(json)
# print the JSON string representation of the object
print
CreateSubmissionResponseIncludedInner.to_json()

# convert the object into a dict
create_submission_response_included_inner_dict = create_submission_response_included_inner_instance.to_dict()
# create an instance of CreateSubmissionResponseIncludedInner from a dict
create_submission_response_included_inner_form_dict = create_submission_response_included_inner.from_dict(
    create_submission_response_included_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


