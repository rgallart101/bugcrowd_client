# ClaimTicket


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
from bugcrowd_client.models.claim_ticket import ClaimTicket

# TODO update the JSON string below
json = "{}"
# create an instance of ClaimTicket from a JSON string
claim_ticket_instance = ClaimTicket.from_json(json)
# print the JSON string representation of the object
print
ClaimTicket.to_json()

# convert the object into a dict
claim_ticket_dict = claim_ticket_instance.to_dict()
# create an instance of ClaimTicket from a dict
claim_ticket_form_dict = claim_ticket.from_dict(claim_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


