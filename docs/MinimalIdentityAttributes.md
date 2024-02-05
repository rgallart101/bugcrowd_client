# MinimalIdentityAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email of the user associated with the identity, not available if the user is a researcher | [optional] 

## Example

```python
from bugcrowd_client.models.minimal_identity_attributes import MinimalIdentityAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of MinimalIdentityAttributes from a JSON string
minimal_identity_attributes_instance = MinimalIdentityAttributes.from_json(json)
# print the JSON string representation of the object
print
MinimalIdentityAttributes.to_json()

# convert the object into a dict
minimal_identity_attributes_dict = minimal_identity_attributes_instance.to_dict()
# create an instance of MinimalIdentityAttributes from a dict
minimal_identity_attributes_form_dict = minimal_identity_attributes.from_dict(minimal_identity_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


