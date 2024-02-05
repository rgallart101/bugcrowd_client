# CreateClaimTicketResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClaimTicket**](ClaimTicket.md) |  | 

## Example

```python
from bugcrowd_client.models.create_claim_ticket_response import CreateClaimTicketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClaimTicketResponse from a JSON string
create_claim_ticket_response_instance = CreateClaimTicketResponse.from_json(json)
# print the JSON string representation of the object
print
CreateClaimTicketResponse.to_json()

# convert the object into a dict
create_claim_ticket_response_dict = create_claim_ticket_response_instance.to_dict()
# create an instance of CreateClaimTicketResponse from a dict
create_claim_ticket_response_form_dict = create_claim_ticket_response.from_dict(create_claim_ticket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


