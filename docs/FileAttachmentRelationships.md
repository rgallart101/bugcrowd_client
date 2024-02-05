# FileAttachmentRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | [**SingleRelationship**](SingleRelationship.md) |  | [optional] 

## Example

```python
from bugcrowd_client.models.file_attachment_relationships import FileAttachmentRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of FileAttachmentRelationships from a JSON string
file_attachment_relationships_instance = FileAttachmentRelationships.from_json(json)
# print the JSON string representation of the object
print
FileAttachmentRelationships.to_json()

# convert the object into a dict
file_attachment_relationships_dict = file_attachment_relationships_instance.to_dict()
# create an instance of FileAttachmentRelationships from a dict
file_attachment_relationships_form_dict = file_attachment_relationships.from_dict(file_attachment_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


