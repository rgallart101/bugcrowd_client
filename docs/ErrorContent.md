# ErrorContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[ErrorContentErrorsInner]**](ErrorContentErrorsInner.md) |  | 

## Example

```python
from bugcrowd_client.models.error_content import ErrorContent

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorContent from a JSON string
error_content_instance = ErrorContent.from_json(json)
# print the JSON string representation of the object
print
ErrorContent.to_json()

# convert the object into a dict
error_content_dict = error_content_instance.to_dict()
# create an instance of ErrorContent from a dict
error_content_form_dict = error_content.from_dict(error_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


