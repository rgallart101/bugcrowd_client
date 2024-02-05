# bugcrowd_client.CommentResourceApi

All URIs are relative to *https://api.bugcrowd.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_comment**](CommentResourceApi.md#create_comment) | **POST** /comments | Create a comment


# **create_comment**
> CreateCommentResponse create_comment(create_comment_request)

Create a comment

Create a comment on a submission

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import os
import bugcrowd_client
from bugcrowd_client.models.create_comment_request import CreateCommentRequest
from bugcrowd_client.models.create_comment_response import CreateCommentResponse
from bugcrowd_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.bugcrowd.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bugcrowd_client.Configuration(
    host="https://api.bugcrowd.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with bugcrowd_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bugcrowd_client.CommentResourceApi(api_client)
    create_comment_request = {"data": {"type": "comment", "attributes": {"body": "comment body",
                                                                         "visibility_scope": "everyone"}}}  # CreateCommentRequest | 

    try:
        # Create a comment
        api_response = api_instance.create_comment(create_comment_request)
        print("The response of CommentResourceApi->create_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentResourceApi->create_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_comment_request** | [**CreateCommentRequest**](CreateCommentRequest.md)|  | 

### Return type

[**CreateCommentResponse**](CreateCommentResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.bugcrowd.v4+json
 - **Accept**: application/vnd.bugcrowd.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comment created |  -  |
**400** | Error indicating malformed request payload |  -  |
**404** | An error indicating missing resource. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**409** | Incorrect data type parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

