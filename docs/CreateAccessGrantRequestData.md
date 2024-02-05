# CreateAccessGrantRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | [**CreateAccessGrantRequestDataAttributes**](CreateAccessGrantRequestDataAttributes.md) |  | 
**relationships** | [**CreateAccessGrantRequestDataRelationships**](CreateAccessGrantRequestDataRelationships.md) |  | 

## Example

```python
from bugcrowd_client.models.create_access_grant_request_data import CreateAccessGrantRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccessGrantRequestData from a JSON string
create_access_grant_request_data_instance = CreateAccessGrantRequestData.from_json(json)
# print the JSON string representation of the object
print
CreateAccessGrantRequestData.to_json()

# convert the object into a dict
create_access_grant_request_data_dict = create_access_grant_request_data_instance.to_dict()
# create an instance of CreateAccessGrantRequestData from a dict
create_access_grant_request_data_form_dict = create_access_grant_request_data.from_dict(
    create_access_grant_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


