# ClaimTicketAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claim_url** | **str** | URL where the claim ticket can be accessed. This value is based on the token and is only available in the response when a claim token is created. | [optional] 
**token** | **str** | Unique token for the claim ticket. This value is not stored and is only available in the response when a claim token is created. | [optional] 
**claimed_at** | **str** | Timestamp indicating that the claim ticket has been claimed and when it was claimed | [optional] 
**expires_at** | **str** | Timestamp indicating when the claim ticket will expire | [optional] 
**status** | [**ClaimTicketStatusEnum**](ClaimTicketStatusEnum.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.claim_ticket_attributes import ClaimTicketAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ClaimTicketAttributes from a JSON string
claim_ticket_attributes_instance = ClaimTicketAttributes.from_json(json)
# print the JSON string representation of the object
print
ClaimTicketAttributes.to_json()

# convert the object into a dict
claim_ticket_attributes_dict = claim_ticket_attributes_instance.to_dict()
# create an instance of ClaimTicketAttributes from a dict
claim_ticket_attributes_form_dict = claim_ticket_attributes.from_dict(claim_ticket_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


