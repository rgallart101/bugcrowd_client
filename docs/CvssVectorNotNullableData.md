# CvssVectorNotNullableData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 

## Example

```python
from bugcrowd_client.models.cvss_vector_not_nullable_data import CvssVectorNotNullableData

# TODO update the JSON string below
json = "{}"
# create an instance of CvssVectorNotNullableData from a JSON string
cvss_vector_not_nullable_data_instance = CvssVectorNotNullableData.from_json(json)
# print the JSON string representation of the object
print
CvssVectorNotNullableData.to_json()

# convert the object into a dict
cvss_vector_not_nullable_data_dict = cvss_vector_not_nullable_data_instance.to_dict()
# create an instance of CvssVectorNotNullableData from a dict
cvss_vector_not_nullable_data_form_dict = cvss_vector_not_nullable_data.from_dict(cvss_vector_not_nullable_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


