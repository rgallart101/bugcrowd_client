# ClaimTicketRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**submissions** | [**ManyRelationship**](ManyRelationship.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.claim_ticket_relationships import ClaimTicketRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ClaimTicketRelationships from a JSON string
claim_ticket_relationships_instance = ClaimTicketRelationships.from_json(json)
# print the JSON string representation of the object
print
ClaimTicketRelationships.to_json()

# convert the object into a dict
claim_ticket_relationships_dict = claim_ticket_relationships_instance.to_dict()
# create an instance of ClaimTicketRelationships from a dict
claim_ticket_relationships_form_dict = claim_ticket_relationships.from_dict(claim_ticket_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


