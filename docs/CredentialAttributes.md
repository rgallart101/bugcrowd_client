# CredentialAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | Unique identifier for the user | [optional] 
**credential_bucket_id** | **str** | Unique identifier for the credential bucket | [optional] 
**data** | **Dict[str, object]** | Data associated with the credential | [optional] 

## Example

```python
from bugcrowd_client.models.credential_attributes import CredentialAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialAttributes from a JSON string
credential_attributes_instance = CredentialAttributes.from_json(json)
# print the JSON string representation of the object
print
CredentialAttributes.to_json()

# convert the object into a dict
credential_attributes_dict = credential_attributes_instance.to_dict()
# create an instance of CredentialAttributes from a dict
credential_attributes_form_dict = credential_attributes.from_dict(credential_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


