# CvssVectorAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attack_complexity** | [**CvssHighLowOptionsEnum**](CvssHighLowOptionsEnum.md) |  | [optional] 
**attack_vector** | [**CvssAttackVectorOptionsEnum**](CvssAttackVectorOptionsEnum.md) |  | [optional] 
**authorization_scope** | [**CvssScopeOptionsEnum**](CvssScopeOptionsEnum.md) |  | [optional] 
**availability_impact** | [**CvssHighLowOptionsEnum**](CvssHighLowOptionsEnum.md) |  | [optional] 
**confidentiality_impact** | [**CvssHighLowOptionsEnum**](CvssHighLowOptionsEnum.md) |  | [optional] 
**integrity_impact** | [**CvssHighLowOptionsEnum**](CvssHighLowOptionsEnum.md) |  | [optional] 
**privileges_required** | [**CvssHighLowOptionsEnum**](CvssHighLowOptionsEnum.md) |  | [optional] 
**score** | **float** |  | [optional] 
**user_interaction** | [**CvssUserInteractionOptionsEnum**](CvssUserInteractionOptionsEnum.md) |  | [optional] 
**version** | **float** | CVSS version number | [optional] 

## Example

```python
from bugcrowd_client.models.cvss_vector_attributes import CvssVectorAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CvssVectorAttributes from a JSON string
cvss_vector_attributes_instance = CvssVectorAttributes.from_json(json)
# print the JSON string representation of the object
print
CvssVectorAttributes.to_json()

# convert the object into a dict
cvss_vector_attributes_dict = cvss_vector_attributes_instance.to_dict()
# create an instance of CvssVectorAttributes from a dict
cvss_vector_attributes_form_dict = cvss_vector_attributes.from_dict(cvss_vector_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


