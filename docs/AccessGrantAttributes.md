# AccessGrantAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | Role granted on the particular resource | [optional] 

## Example

```python
from bugcrowd_client.models.access_grant_attributes import AccessGrantAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AccessGrantAttributes from a JSON string
access_grant_attributes_instance = AccessGrantAttributes.from_json(json)
# print the JSON string representation of the object
print
AccessGrantAttributes.to_json()

# convert the object into a dict
access_grant_attributes_dict = access_grant_attributes_instance.to_dict()
# create an instance of AccessGrantAttributes from a dict
access_grant_attributes_form_dict = access_grant_attributes.from_dict(access_grant_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


