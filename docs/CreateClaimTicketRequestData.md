# CreateClaimTicketRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | **object** |  | [optional] 
**relationships** | [**CreateClaimTicketRequestDataRelationships**](CreateClaimTicketRequestDataRelationships.md) |  | 

## Example

```python
from bugcrowd_client.models.create_claim_ticket_request_data import CreateClaimTicketRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClaimTicketRequestData from a JSON string
create_claim_ticket_request_data_instance = CreateClaimTicketRequestData.from_json(json)
# print the JSON string representation of the object
print
CreateClaimTicketRequestData.to_json()

# convert the object into a dict
create_claim_ticket_request_data_dict = create_claim_ticket_request_data_instance.to_dict()
# create an instance of CreateClaimTicketRequestData from a dict
create_claim_ticket_request_data_form_dict = create_claim_ticket_request_data.from_dict(
    create_claim_ticket_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


