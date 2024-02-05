# IdentityAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | For researchers this will have the researcher&#39;s username if they are public, otherwise it will show &#39;a private user&#39;.  For non-researcher identities (Customer team or Bugcrowd staff) this will show the user&#39;s &#x60;display_name&#x60; if set, otherwise it will show &#39;a Crowdcontrol user&#39;.  | [optional] 
**email** | **str** | For researchers this property is not provided at all, this key will be absent from the attributes object.  For non-researcher identities (Customer team or Bugcrowd staff), this property will contain the unique email for the user associated with the identity.  | [optional] 
**staff** | **bool** | Indicates whether the user associated with the identity is staff | [optional] 

## Example

```python
from bugcrowd_client.models.identity_attributes import IdentityAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAttributes from a JSON string
identity_attributes_instance = IdentityAttributes.from_json(json)
# print the JSON string representation of the object
print
IdentityAttributes.to_json()

# convert the object into a dict
identity_attributes_dict = identity_attributes_instance.to_dict()
# create an instance of IdentityAttributes from a dict
identity_attributes_form_dict = identity_attributes.from_dict(identity_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


