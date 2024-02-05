# CvssVector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 
**attributes** | [**CvssVectorAttributes**](CvssVectorAttributes.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from bugcrowd_client.models.cvss_vector import CvssVector

# TODO update the JSON string below
json = "{}"
# create an instance of CvssVector from a JSON string
cvss_vector_instance = CvssVector.from_json(json)
# print the JSON string representation of the object
print
CvssVector.to_json()

# convert the object into a dict
cvss_vector_dict = cvss_vector_instance.to_dict()
# create an instance of CvssVector from a dict
cvss_vector_form_dict = cvss_vector.from_dict(cvss_vector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


