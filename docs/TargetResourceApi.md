# bugcrowd_client.TargetResourceApi

All URIs are relative to *https://api.bugcrowd.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_targets**](TargetResourceApi.md#list_targets) | **GET** /targets | Index targets


# **list_targets**
> ListTargetsResponse list_targets(bugcrowd_version=bugcrowd_version, fields_organization=fields_organization, fields_target=fields_target, page_limit=page_limit, page_offset=page_offset, filter_organization_id=filter_organization_id, include=include, filter_target_group_id=filter_target_group_id)

Index targets

Returns a list of targets belonging to the organizations of the user.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import os
import bugcrowd_client
from bugcrowd_client.models.list_targets_response import ListTargetsResponse
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
    api_instance = bugcrowd_client.TargetResourceApi(api_client)
    bugcrowd_version = '{\"$ref\":\"#/info/version\"}'  # str | The request header used to test new API versions before updating the pinned account version (optional)
    fields_organization = [
        'name,programs']  # List[str] | Limit fields for `organization` resources. If not provided, all fields will be returned (optional)
    fields_target = [
        'name,category']  # List[str] | Limit fields for `target` resources. If not provided, all fields will be returned (optional)
    page_limit = 25  # int | Limit parameter for pagination (default page[limit] = 25) (optional) (default to 25)
    page_offset = 0  # int | Offset parameter for pagination (default page[offset] = 0 == first page) (optional) (default to 0)
    filter_organization_id = [
        '{\"$ref\":\"https://bugcrowd.com/openapi/2024-01-11/external_elements.yml#/general_helpers/ValidUUID\"}']  # List[str] | Filter by the UUID of the organization they belong to. (optional)
    include = [
        'organization']  # List[str] | Related associations that will be returned as a flat list of objects. (optional)
    filter_target_group_id = [
        '5']  # List[str] | Filter targets by the group they belong to (Used to paginate targets on a program) (optional)

    try:
        # Index targets
        api_response = api_instance.list_targets(bugcrowd_version=bugcrowd_version,
                                                 fields_organization=fields_organization, fields_target=fields_target,
                                                 page_limit=page_limit, page_offset=page_offset,
                                                 filter_organization_id=filter_organization_id, include=include,
                                                 filter_target_group_id=filter_target_group_id)
        print("The response of TargetResourceApi->list_targets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TargetResourceApi->list_targets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bugcrowd_version** | **str**| The request header used to test new API versions before updating the pinned account version | [optional] 
 **fields_organization** | [**List[str]**](str.md)| Limit fields for &#x60;organization&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_target** | [**List[str]**](str.md)| Limit fields for &#x60;target&#x60; resources. If not provided, all fields will be returned | [optional] 
 **page_limit** | **int**| Limit parameter for pagination (default page[limit] &#x3D; 25) | [optional] [default to 25]
 **page_offset** | **int**| Offset parameter for pagination (default page[offset] &#x3D; 0 &#x3D;&#x3D; first page) | [optional] [default to 0]
 **filter_organization_id** | [**List[str]**](str.md)| Filter by the UUID of the organization they belong to. | [optional] 
 **include** | [**List[str]**](str.md)| Related associations that will be returned as a flat list of objects. | [optional] 
 **filter_target_group_id** | [**List[str]**](str.md)| Filter targets by the group they belong to (Used to paginate targets on a program) | [optional] 

### Return type

[**ListTargetsResponse**](ListTargetsResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bugcrowd.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a &#x60;data&#x60; property containing an array of target objects. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**400** | An error object indicating unsupported request parameters. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**404** | An error indicating missing resource. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

