# MinimalIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | 
**attributes** | [**MinimalIdentityAttributes**](MinimalIdentityAttributes.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from bugcrowd_client.models.minimal_identity import MinimalIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of MinimalIdentity from a JSON string
minimal_identity_instance = MinimalIdentity.from_json(json)
# print the JSON string representation of the object
print
MinimalIdentity.to_json()

# convert the object into a dict
minimal_identity_dict = minimal_identity_instance.to_dict()
# create an instance of MinimalIdentity from a dict
minimal_identity_form_dict = minimal_identity.from_dict(minimal_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


