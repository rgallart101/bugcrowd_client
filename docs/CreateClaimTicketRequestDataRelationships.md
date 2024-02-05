# CreateClaimTicketRequestDataRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**submissions** | [**SubmissionsMax1**](SubmissionsMax1.md) |  | 

## Example

```python
from bugcrowd_client.models.create_claim_ticket_request_data_relationships import
    CreateClaimTicketRequestDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClaimTicketRequestDataRelationships from a JSON string
create_claim_ticket_request_data_relationships_instance = CreateClaimTicketRequestDataRelationships.from_json(json)
# print the JSON string representation of the object
print
CreateClaimTicketRequestDataRelationships.to_json()

# convert the object into a dict
create_claim_ticket_request_data_relationships_dict = create_claim_ticket_request_data_relationships_instance.to_dict()
# create an instance of CreateClaimTicketRequestDataRelationships from a dict
create_claim_ticket_request_data_relationships_form_dict = create_claim_ticket_request_data_relationships.from_dict(
    create_claim_ticket_request_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


