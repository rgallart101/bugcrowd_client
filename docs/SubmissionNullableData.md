# SubmissionNullableData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 

## Example

```python
from bugcrowd_client.models.submission_nullable_data import SubmissionNullableData

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionNullableData from a JSON string
submission_nullable_data_instance = SubmissionNullableData.from_json(json)
# print the JSON string representation of the object
print
SubmissionNullableData.to_json()

# convert the object into a dict
submission_nullable_data_dict = submission_nullable_data_instance.to_dict()
# create an instance of SubmissionNullableData from a dict
submission_nullable_data_form_dict = submission_nullable_data.from_dict(submission_nullable_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


