# SubmissionRelationships

All relationships to the submission.  _The following relationships are only available with direct access to the submission's program:_  - activities - assignee - comments - file_attachments - monetary_rewards 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activities** | [**ManyRelationship**](ManyRelationship.md) |  | [optional] 
**assignee** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 
**program** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 
**claim_ticket** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 
**comments** | [**ManyRelationship**](ManyRelationship.md) |  | [optional] 
**cvss_vector** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 
**duplicates** | [**ManyRelationship**](ManyRelationship.md) |  | [optional] 
**duplicate_of** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 
**external_issues** | [**ManyRelationship**](ManyRelationship.md) |  | [optional] 
**file_attachments** | [**ManyRelationship**](ManyRelationship.md) |  | [optional] 
**monetary_rewards** | [**ManyRelationship**](ManyRelationship.md) |  | [optional] 
**target** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 
**researcher** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.submission_relationships import SubmissionRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionRelationships from a JSON string
submission_relationships_instance = SubmissionRelationships.from_json(json)
# print the JSON string representation of the object
print
SubmissionRelationships.to_json()

# convert the object into a dict
submission_relationships_dict = submission_relationships_instance.to_dict()
# create an instance of SubmissionRelationships from a dict
submission_relationships_form_dict = submission_relationships.from_dict(submission_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


