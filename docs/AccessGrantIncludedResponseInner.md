# AccessGrantIncludedResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | 
**attributes** | [**OrganizationAttributes**](OrganizationAttributes.md) |  | [optional] 
**relationships** | [**OrganizationRelationships**](OrganizationRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.access_grant_included_response_inner import AccessGrantIncludedResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccessGrantIncludedResponseInner from a JSON string
access_grant_included_response_inner_instance = AccessGrantIncludedResponseInner.from_json(json)
# print the JSON string representation of the object
print
AccessGrantIncludedResponseInner.to_json()

# convert the object into a dict
access_grant_included_response_inner_dict = access_grant_included_response_inner_instance.to_dict()
# create an instance of AccessGrantIncludedResponseInner from a dict
access_grant_included_response_inner_form_dict = access_grant_included_response_inner.from_dict(
    access_grant_included_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


