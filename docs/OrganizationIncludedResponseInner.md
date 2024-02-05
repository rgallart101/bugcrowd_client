# OrganizationIncludedResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 
**attributes** | [**TargetAttributes**](TargetAttributes.md) |  | [optional] 
**relationships** | [**TargetRelationships**](TargetRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.organization_included_response_inner import OrganizationIncludedResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationIncludedResponseInner from a JSON string
organization_included_response_inner_instance = OrganizationIncludedResponseInner.from_json(json)
# print the JSON string representation of the object
print
OrganizationIncludedResponseInner.to_json()

# convert the object into a dict
organization_included_response_inner_dict = organization_included_response_inner_instance.to_dict()
# create an instance of OrganizationIncludedResponseInner from a dict
organization_included_response_inner_form_dict = organization_included_response_inner.from_dict(
    organization_included_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


