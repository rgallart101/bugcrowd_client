# bugcrowd_client.OrganizationResourceApi

All URIs are relative to *https://api.bugcrowd.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organization**](OrganizationResourceApi.md#get_organization) | **GET** /organizations/{id} | Fetch organization
[**list_organizations**](OrganizationResourceApi.md#list_organizations) | **GET** /organizations | Index organizations


# **get_organization**
> GetOrganizationResponse get_organization(id, bugcrowd_version=bugcrowd_version, fields_organization=fields_organization, fields_program=fields_program, fields_target=fields_target, include=include)

Fetch organization

Returns a single organization by UUID.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import os
import bugcrowd_client
from bugcrowd_client.models.get_organization_response import GetOrganizationResponse
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
    api_instance = bugcrowd_client.OrganizationResourceApi(api_client)
    id = '{\"$ref\":\"https://bugcrowd.com/openapi/2024-01-11/external_elements.yml#/general_helpers/ValidUUID\"}'  # str | The ID of the resource in uuid format
    bugcrowd_version = '{\"$ref\":\"#/info/version\"}'  # str | The request header used to test new API versions before updating the pinned account version (optional)
    fields_organization = [
        'name,programs']  # List[str] | Limit fields for `organization` resources. If not provided, all fields will be returned (optional)
    fields_program = [
        'code,organization']  # List[str] | Limit fields for `program` resources. If not provided, all fields will be returned (optional)
    fields_target = [
        'name,category']  # List[str] | Limit fields for `target` resources. If not provided, all fields will be returned (optional)
    include = [
        'targets']  # List[str] | Related associations that will be returned as a flat list of objects. (optional)

    try:
        # Fetch organization
        api_response = api_instance.get_organization(id, bugcrowd_version=bugcrowd_version,
                                                     fields_organization=fields_organization,
                                                     fields_program=fields_program, fields_target=fields_target,
                                                     include=include)
        print("The response of OrganizationResourceApi->get_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationResourceApi->get_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource in uuid format | 
 **bugcrowd_version** | **str**| The request header used to test new API versions before updating the pinned account version | [optional] 
 **fields_organization** | [**List[str]**](str.md)| Limit fields for &#x60;organization&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_program** | [**List[str]**](str.md)| Limit fields for &#x60;program&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_target** | [**List[str]**](str.md)| Limit fields for &#x60;target&#x60; resources. If not provided, all fields will be returned | [optional] 
 **include** | [**List[str]**](str.md)| Related associations that will be returned as a flat list of objects. | [optional] 

### Return type

[**GetOrganizationResponse**](GetOrganizationResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bugcrowd.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a &#x60;data&#x60; property containing an organization object. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**400** | An error object indicating unsupported request parameters. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**404** | An error indicating missing resource. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organizations**
> ListOrganizationsResponse list_organizations(bugcrowd_version=bugcrowd_version, fields_organization=fields_organization, fields_program=fields_program, fields_target=fields_target, page_limit=page_limit, page_offset=page_offset, include=include, sort=sort)

Index organizations

Returns a list of organizations belonging to the user.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import os
import bugcrowd_client
from bugcrowd_client.models.list_organizations_response import ListOrganizationsResponse
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
    api_instance = bugcrowd_client.OrganizationResourceApi(api_client)
    bugcrowd_version = '{\"$ref\":\"#/info/version\"}'  # str | The request header used to test new API versions before updating the pinned account version (optional)
    fields_organization = [
        'name,programs']  # List[str] | Limit fields for `organization` resources. If not provided, all fields will be returned (optional)
    fields_program = [
        'code,organization']  # List[str] | Limit fields for `program` resources. If not provided, all fields will be returned (optional)
    fields_target = [
        'name,category']  # List[str] | Limit fields for `target` resources. If not provided, all fields will be returned (optional)
    page_limit = 25  # int | Limit parameter for pagination (default page[limit] = 25) (optional) (default to 25)
    page_offset = 0  # int | Offset parameter for pagination (default page[offset] = 0 == first page) (optional) (default to 0)
    include = [
        'programs']  # List[str] | Related associations that will be returned as a flat list of objects. (optional)
    sort = ['name-desc']  # List[str] | Sorting options (optional)

    try:
        # Index organizations
        api_response = api_instance.list_organizations(bugcrowd_version=bugcrowd_version,
                                                       fields_organization=fields_organization,
                                                       fields_program=fields_program, fields_target=fields_target,
                                                       page_limit=page_limit, page_offset=page_offset, include=include,
                                                       sort=sort)
        print("The response of OrganizationResourceApi->list_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationResourceApi->list_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bugcrowd_version** | **str**| The request header used to test new API versions before updating the pinned account version | [optional] 
 **fields_organization** | [**List[str]**](str.md)| Limit fields for &#x60;organization&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_program** | [**List[str]**](str.md)| Limit fields for &#x60;program&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_target** | [**List[str]**](str.md)| Limit fields for &#x60;target&#x60; resources. If not provided, all fields will be returned | [optional] 
 **page_limit** | **int**| Limit parameter for pagination (default page[limit] &#x3D; 25) | [optional] [default to 25]
 **page_offset** | **int**| Offset parameter for pagination (default page[offset] &#x3D; 0 &#x3D;&#x3D; first page) | [optional] [default to 0]
 **include** | [**List[str]**](str.md)| Related associations that will be returned as a flat list of objects. | [optional] 
 **sort** | [**List[str]**](str.md)| Sorting options | [optional] 

### Return type

[**ListOrganizationsResponse**](ListOrganizationsResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bugcrowd.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a &#x60;data&#x60; property containing an array of organization objects. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**400** | An error object indicating unsupported request parameters. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**404** | An error indicating missing resource. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

