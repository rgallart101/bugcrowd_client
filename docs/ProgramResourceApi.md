# bugcrowd_client.ProgramResourceApi

All URIs are relative to *https://api.bugcrowd.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_program**](ProgramResourceApi.md#get_program) | **GET** /programs/{id} | Fetch program
[**list_programs**](ProgramResourceApi.md#list_programs) | **GET** /programs | Index programs


# **get_program**
> GetProgramResponse get_program(id, bugcrowd_version=bugcrowd_version, fields_organization=fields_organization, fields_program=fields_program, fields_program_brief=fields_program_brief, fields_reward_range=fields_reward_range, fields_submission=fields_submission, fields_target=fields_target, fields_target_group=fields_target_group, include=include)

Fetch program

Returns a single program by UUID.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import os
import bugcrowd_client
from bugcrowd_client.models.get_program_response import GetProgramResponse
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
    api_instance = bugcrowd_client.ProgramResourceApi(api_client)
    id = '{\"$ref\":\"https://bugcrowd.com/openapi/2024-01-11/external_elements.yml#/general_helpers/ValidUUID\"}'  # str | The ID of the resource in uuid format
    bugcrowd_version = '{\"$ref\":\"#/info/version\"}'  # str | The request header used to test new API versions before updating the pinned account version (optional)
    fields_organization = [
        'name,programs']  # List[str] | Limit fields for `organization` resources. If not provided, all fields will be returned (optional)
    fields_program = [
        'code,organization']  # List[str] | Limit fields for `program` resources. If not provided, all fields will be returned (optional)
    fields_program_brief = [
        'demo,program']  # List[str] | Limit fields for `program_brief` resources. If not provided, all fields will be returned (optional)
    fields_reward_range = [
        'p1_max_cents,p1_min_cents']  # List[str] | Limit fields for `reward_range` resources. If not provided, all fields will be returned (optional)
    fields_submission = [
        'state,duplicate']  # List[str] | Limit fields for `submission` resources. If not provided, all fields will be returned (optional)
    fields_target = [
        'name,category']  # List[str] | Limit fields for `target` resources. If not provided, all fields will be returned (optional)
    fields_target_group = [
        'name,in_scope']  # List[str] | Limit fields for `target_group` resources. If not provided, all fields will be returned (optional)
    include = [
        'current_brief']  # List[str] | Related associations that will be returned as a flat list of objects. (optional)

    try:
        # Fetch program
        api_response = api_instance.get_program(id, bugcrowd_version=bugcrowd_version,
                                                fields_organization=fields_organization, fields_program=fields_program,
                                                fields_program_brief=fields_program_brief,
                                                fields_reward_range=fields_reward_range,
                                                fields_submission=fields_submission, fields_target=fields_target,
                                                fields_target_group=fields_target_group, include=include)
        print("The response of ProgramResourceApi->get_program:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProgramResourceApi->get_program: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource in uuid format | 
 **bugcrowd_version** | **str**| The request header used to test new API versions before updating the pinned account version | [optional] 
 **fields_organization** | [**List[str]**](str.md)| Limit fields for &#x60;organization&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_program** | [**List[str]**](str.md)| Limit fields for &#x60;program&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_program_brief** | [**List[str]**](str.md)| Limit fields for &#x60;program_brief&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_reward_range** | [**List[str]**](str.md)| Limit fields for &#x60;reward_range&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_submission** | [**List[str]**](str.md)| Limit fields for &#x60;submission&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_target** | [**List[str]**](str.md)| Limit fields for &#x60;target&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_target_group** | [**List[str]**](str.md)| Limit fields for &#x60;target_group&#x60; resources. If not provided, all fields will be returned | [optional] 
 **include** | [**List[str]**](str.md)| Related associations that will be returned as a flat list of objects. | [optional] 

### Return type

[**GetProgramResponse**](GetProgramResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bugcrowd.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a &#x60;data&#x60; property containing a program object. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**400** | An error object indicating unsupported request parameters. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**404** | An error indicating missing resource. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_programs**
> ListProgramsResponse list_programs(bugcrowd_version=bugcrowd_version, fields_organization=fields_organization, fields_program=fields_program, fields_program_brief=fields_program_brief, fields_reward_range=fields_reward_range, fields_submission=fields_submission, fields_target=fields_target, fields_target_group=fields_target_group, page_limit=page_limit, page_offset=page_offset, include=include, filter_organization_id=filter_organization_id, sort=sort)

Index programs

Returns a list of programs belonging to the user.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import os
import bugcrowd_client
from bugcrowd_client.models.list_programs_response import ListProgramsResponse
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
    api_instance = bugcrowd_client.ProgramResourceApi(api_client)
    bugcrowd_version = '{\"$ref\":\"#/info/version\"}'  # str | The request header used to test new API versions before updating the pinned account version (optional)
    fields_organization = [
        'name,programs']  # List[str] | Limit fields for `organization` resources. If not provided, all fields will be returned (optional)
    fields_program = [
        'code,organization']  # List[str] | Limit fields for `program` resources. If not provided, all fields will be returned (optional)
    fields_program_brief = [
        'demo,program']  # List[str] | Limit fields for `program_brief` resources. If not provided, all fields will be returned (optional)
    fields_reward_range = [
        'p1_max_cents,p1_min_cents']  # List[str] | Limit fields for `reward_range` resources. If not provided, all fields will be returned (optional)
    fields_submission = [
        'state,duplicate']  # List[str] | Limit fields for `submission` resources. If not provided, all fields will be returned (optional)
    fields_target = [
        'name,category']  # List[str] | Limit fields for `target` resources. If not provided, all fields will be returned (optional)
    fields_target_group = [
        'name,in_scope']  # List[str] | Limit fields for `target_group` resources. If not provided, all fields will be returned (optional)
    page_limit = 25  # int | Limit parameter for pagination (default page[limit] = 25) (optional) (default to 25)
    page_offset = 0  # int | Offset parameter for pagination (default page[offset] = 0 == first page) (optional) (default to 0)
    include = [
        'current_brief']  # List[str] | Related associations that will be returned as a flat list of objects. (optional)
    filter_organization_id = [
        '{\"$ref\":\"https://bugcrowd.com/openapi/2024-01-11/external_elements.yml#/general_helpers/ValidUUID\"}']  # List[str] | Filter by the UUID of the organization they belong to. (optional)
    sort = ['promoted-desc,starts-desc']  # List[str] | Tokenized search sort options (optional)

    try:
        # Index programs
        api_response = api_instance.list_programs(bugcrowd_version=bugcrowd_version,
                                                  fields_organization=fields_organization,
                                                  fields_program=fields_program,
                                                  fields_program_brief=fields_program_brief,
                                                  fields_reward_range=fields_reward_range,
                                                  fields_submission=fields_submission, fields_target=fields_target,
                                                  fields_target_group=fields_target_group, page_limit=page_limit,
                                                  page_offset=page_offset, include=include,
                                                  filter_organization_id=filter_organization_id, sort=sort)
        print("The response of ProgramResourceApi->list_programs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProgramResourceApi->list_programs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bugcrowd_version** | **str**| The request header used to test new API versions before updating the pinned account version | [optional] 
 **fields_organization** | [**List[str]**](str.md)| Limit fields for &#x60;organization&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_program** | [**List[str]**](str.md)| Limit fields for &#x60;program&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_program_brief** | [**List[str]**](str.md)| Limit fields for &#x60;program_brief&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_reward_range** | [**List[str]**](str.md)| Limit fields for &#x60;reward_range&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_submission** | [**List[str]**](str.md)| Limit fields for &#x60;submission&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_target** | [**List[str]**](str.md)| Limit fields for &#x60;target&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_target_group** | [**List[str]**](str.md)| Limit fields for &#x60;target_group&#x60; resources. If not provided, all fields will be returned | [optional] 
 **page_limit** | **int**| Limit parameter for pagination (default page[limit] &#x3D; 25) | [optional] [default to 25]
 **page_offset** | **int**| Offset parameter for pagination (default page[offset] &#x3D; 0 &#x3D;&#x3D; first page) | [optional] [default to 0]
 **include** | [**List[str]**](str.md)| Related associations that will be returned as a flat list of objects. | [optional] 
 **filter_organization_id** | [**List[str]**](str.md)| Filter by the UUID of the organization they belong to. | [optional] 
 **sort** | [**List[str]**](str.md)| Tokenized search sort options | [optional] 

### Return type

[**ListProgramsResponse**](ListProgramsResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bugcrowd.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a &#x60;data&#x60; property containing an array of program objects. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**400** | An error object indicating unsupported request parameters. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**404** | An error indicating missing resource. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

