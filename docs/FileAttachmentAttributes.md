# FileAttachmentAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | The name of the file | [optional] 
**file_size** | **int** | Size of the file in bytes | [optional] 
**file_type** | **str** | Filetype. Some examples include &#39;image/png&#39; and &#39;application/zip&#39; | [optional] 
**download_url** | **str** | An authenticated endpoint that looks like &#x60;files.bugcrowd.com/:file_attachment_id&#x60;  To use this URL you must include the API &#39;Authorization&#39; header and it will redirect to a signed s3 URL with a 10 second expiry.  This way you can store the &#x60;download_url&#x60; and it will not expire, but the s3 link is kept secure.  WARNING: DO NOT USE cURL -L to follow the s3 redirect CVE: https://curl.se/docs/CVE-2018-1000007.html  Versions below 7.58.0 automatically forward the authorization headers  In later versions we will introduce OAuth which will somewhat mitigate the risk involved with the authorization header as it will expire.  | [optional] 
**s3_signed_url** | **str** | URL to the file attachment download.  This link expires in 1 minute and encodes &#x60;&amp;&#x60; as &#x60;\\u0026&#x60;.  The &#x60;\\u0026&#x60; must be replaced with &#x60;&amp;&#x60; for the link to work.  [DEPRECATED] - This attribute will be removed in a future version, use &#x60;download_url&#x60; instead.  | [optional] 

## Example

```python
from bugcrowd_client.models.file_attachment_attributes import FileAttachmentAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of FileAttachmentAttributes from a JSON string
file_attachment_attributes_instance = FileAttachmentAttributes.from_json(json)
# print the JSON string representation of the object
print
FileAttachmentAttributes.to_json()

# convert the object into a dict
file_attachment_attributes_dict = file_attachment_attributes_instance.to_dict()
# create an instance of FileAttachmentAttributes from a dict
file_attachment_attributes_form_dict = file_attachment_attributes.from_dict(file_attachment_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


