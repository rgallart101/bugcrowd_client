# CreateClaimTicketRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateClaimTicketRequestData**](CreateClaimTicketRequestData.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.create_claim_ticket_request import CreateClaimTicketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClaimTicketRequest from a JSON string
create_claim_ticket_request_instance = CreateClaimTicketRequest.from_json(json)
# print the JSON string representation of the object
print
CreateClaimTicketRequest.to_json()

# convert the object into a dict
create_claim_ticket_request_dict = create_claim_ticket_request_instance.to_dict()
# create an instance of CreateClaimTicketRequest from a dict
create_claim_ticket_request_form_dict = create_claim_ticket_request.from_dict(create_claim_ticket_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


