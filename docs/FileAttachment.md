# FileAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the resource | 
**type** | **str** |  | 
**links** | [**SelfLink**](SelfLink.md) |  | [optional] 
**attributes** | [**FileAttachmentAttributes**](FileAttachmentAttributes.md) |  | [optional] 
**relationships** | [**FileAttachmentRelationships**](FileAttachmentRelationships.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.file_attachment import FileAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of FileAttachment from a JSON string
file_attachment_instance = FileAttachment.from_json(json)
# print the JSON string representation of the object
print
FileAttachment.to_json()

# convert the object into a dict
file_attachment_dict = file_attachment_instance.to_dict()
# create an instance of FileAttachment from a dict
file_attachment_form_dict = file_attachment.from_dict(file_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


