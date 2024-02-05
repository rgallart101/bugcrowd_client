# ErrorContentErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**detail** | **str** |  | 
**title** | **str** |  | 
**source** | [**ErrorContentErrorsInnerSource**](ErrorContentErrorsInnerSource.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.error_content_errors_inner import ErrorContentErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorContentErrorsInner from a JSON string
error_content_errors_inner_instance = ErrorContentErrorsInner.from_json(json)
# print the JSON string representation of the object
print
ErrorContentErrorsInner.to_json()

# convert the object into a dict
error_content_errors_inner_dict = error_content_errors_inner_instance.to_dict()
# create an instance of ErrorContentErrorsInner from a dict
error_content_errors_inner_form_dict = error_content_errors_inner.from_dict(error_content_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


