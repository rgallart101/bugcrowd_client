# AccessGrant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 
**attributes** | [**AccessGrantAttributes**](AccessGrantAttributes.md) |  | [optional] 
**relationships** | [**AccessGrantRelationships**](AccessGrantRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.access_grant import AccessGrant

# TODO update the JSON string below
json = "{}"
# create an instance of AccessGrant from a JSON string
access_grant_instance = AccessGrant.from_json(json)
# print the JSON string representation of the object
print
AccessGrant.to_json()

# convert the object into a dict
access_grant_dict = access_grant_instance.to_dict()
# create an instance of AccessGrant from a dict
access_grant_form_dict = access_grant.from_dict(access_grant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


