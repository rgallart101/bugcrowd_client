# bugcrowd_client.SubmissionResourceApi

All URIs are relative to *https://api.bugcrowd.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_submission**](SubmissionResourceApi.md#create_submission) | **POST** /submissions | Create submission
[**get_submission**](SubmissionResourceApi.md#get_submission) | **GET** /submissions/{id} | Fetch submission
[**list_submissions**](SubmissionResourceApi.md#list_submissions) | **GET** /submissions | Index submissions
[**update_submission**](SubmissionResourceApi.md#update_submission) | **PATCH** /submissions/{id} | Update submission


# **create_submission**
> CreateSubmissionResponse create_submission(create_submission_request)

Create submission

Create a submission within a program.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import os
import bugcrowd_client
from bugcrowd_client.models.create_submission_request import CreateSubmissionRequest
from bugcrowd_client.models.create_submission_response import CreateSubmissionResponse
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
    api_instance = bugcrowd_client.SubmissionResourceApi(api_client)
    create_submission_request = {"data": {"type": "submission", "attributes": {"title": "This is a good title",
                                                                               "description": "This contains a POC"},
                                          "relationships": {"program": {"data": {"type": "program", "id": {
                                              "$ref": "https://bugcrowd.com/openapi/2024-01-11/external_elements.yml#/general_helpers/ValidUUID"}}}}}}  # CreateSubmissionRequest | A submission resource with a program relationship and an optional target relationship.

    try:
        # Create submission
        api_response = api_instance.create_submission(create_submission_request)
        print("The response of SubmissionResourceApi->create_submission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubmissionResourceApi->create_submission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_submission_request** | [**CreateSubmissionRequest**](CreateSubmissionRequest.md)| A submission resource with a program relationship and an optional target relationship. | 

### Return type

[**CreateSubmissionResponse**](CreateSubmissionResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.bugcrowd.v4+json
 - **Accept**: application/vnd.bugcrowd.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Submission created |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**400** | Bad request |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**403** | Forbidden client-generated ID |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**404** | An error indicating missing resource. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**409** | Incorrect data type parameter |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**422** | Required attributes were not provided. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submission**
> GetSubmissionResponse get_submission(id, bugcrowd_version=bugcrowd_version, fields_activity=fields_activity, fields_claim_ticket=fields_claim_ticket, fields_comment=fields_comment, fields_cvss_vector=fields_cvss_vector, fields_external_issue=fields_external_issue, fields_file_attachment=fields_file_attachment, fields_identity=fields_identity, fields_monetary_reward=fields_monetary_reward, fields_organization=fields_organization, fields_payment=fields_payment, fields_program=fields_program, fields_program_brief=fields_program_brief, fields_submission=fields_submission, fields_target=fields_target, fields_target_group=fields_target_group, include=include)

Fetch submission

Returns a single submission by UUID.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import os
import bugcrowd_client
from bugcrowd_client.models.get_submission_response import GetSubmissionResponse
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
    api_instance = bugcrowd_client.SubmissionResourceApi(api_client)
    id = '{\"$ref\":\"https://bugcrowd.com/openapi/2024-01-11/external_elements.yml#/general_helpers/ValidUUID\"}'  # str | The ID of the resource in uuid format
    bugcrowd_version = '{\"$ref\":\"#/info/version\"}'  # str | The request header used to test new API versions before updating the pinned account version (optional)
    fields_activity = [
        'key,submission']  # List[str] | Limit fields for `activity` resources. If not provided, all fields will be returned (optional)
    fields_claim_ticket = [
        'status,claimed_at']  # List[str] | Limit fields for `claim_ticket` resources. If not provided, all fields will be returned (optional)
    fields_comment = [
        'body,author']  # List[str] | Limit fields for `comment` resources. If not provided, all fields will be returned (optional)
    fields_cvss_vector = [
        'version,score']  # List[str] | Limit fields for `cvss_vector` resources. If not provided, all fields will be returned (optional)
    fields_external_issue = [
        'remote_url,remote_id,resource,integration']  # List[str] | Limit fields for `external_issue` resources. If not provided, all fields will be returned (optional)
    fields_file_attachment = [
        'file_name,download_url']  # List[str] | Limit fields for `file_attachment` resources. If not provided, all fields will be returned (optional)
    fields_identity = [
        'name,email']  # List[str] | Limit fields for `identity` resources. If not provided, all fields will be returned (optional)
    fields_monetary_reward = [
        'formatted_amount,cancelled_at']  # List[str] | Limit fields for `monetary_reward` resources. If not provided, all fields will be returned (optional)
    fields_organization = [
        'name,programs']  # List[str] | Limit fields for `organization` resources. If not provided, all fields will be returned (optional)
    fields_payment = [
        'amount_cents,monetary_reward']  # List[str] | Limit fields for `payment` resources. If not provided, all fields will be returned (optional)
    fields_program = [
        'code,organization']  # List[str] | Limit fields for `program` resources. If not provided, all fields will be returned (optional)
    fields_program_brief = [
        'demo,program']  # List[str] | Limit fields for `program_brief` resources. If not provided, all fields will be returned (optional)
    fields_submission = [
        'state,duplicate']  # List[str] | Limit fields for `submission` resources. If not provided, all fields will be returned (optional)
    fields_target = [
        'name,category']  # List[str] | Limit fields for `target` resources. If not provided, all fields will be returned (optional)
    fields_target_group = [
        'name,in_scope']  # List[str] | Limit fields for `target_group` resources. If not provided, all fields will be returned (optional)
    include = [
        'program']  # List[str] | Related associations that will be returned as a flat list of objects. (optional)

    try:
        # Fetch submission
        api_response = api_instance.get_submission(id, bugcrowd_version=bugcrowd_version,
                                                   fields_activity=fields_activity,
                                                   fields_claim_ticket=fields_claim_ticket,
                                                   fields_comment=fields_comment, fields_cvss_vector=fields_cvss_vector,
                                                   fields_external_issue=fields_external_issue,
                                                   fields_file_attachment=fields_file_attachment,
                                                   fields_identity=fields_identity,
                                                   fields_monetary_reward=fields_monetary_reward,
                                                   fields_organization=fields_organization,
                                                   fields_payment=fields_payment, fields_program=fields_program,
                                                   fields_program_brief=fields_program_brief,
                                                   fields_submission=fields_submission, fields_target=fields_target,
                                                   fields_target_group=fields_target_group, include=include)
        print("The response of SubmissionResourceApi->get_submission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubmissionResourceApi->get_submission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource in uuid format | 
 **bugcrowd_version** | **str**| The request header used to test new API versions before updating the pinned account version | [optional] 
 **fields_activity** | [**List[str]**](str.md)| Limit fields for &#x60;activity&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_claim_ticket** | [**List[str]**](str.md)| Limit fields for &#x60;claim_ticket&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_comment** | [**List[str]**](str.md)| Limit fields for &#x60;comment&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_cvss_vector** | [**List[str]**](str.md)| Limit fields for &#x60;cvss_vector&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_external_issue** | [**List[str]**](str.md)| Limit fields for &#x60;external_issue&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_file_attachment** | [**List[str]**](str.md)| Limit fields for &#x60;file_attachment&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_identity** | [**List[str]**](str.md)| Limit fields for &#x60;identity&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_monetary_reward** | [**List[str]**](str.md)| Limit fields for &#x60;monetary_reward&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_organization** | [**List[str]**](str.md)| Limit fields for &#x60;organization&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_payment** | [**List[str]**](str.md)| Limit fields for &#x60;payment&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_program** | [**List[str]**](str.md)| Limit fields for &#x60;program&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_program_brief** | [**List[str]**](str.md)| Limit fields for &#x60;program_brief&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_submission** | [**List[str]**](str.md)| Limit fields for &#x60;submission&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_target** | [**List[str]**](str.md)| Limit fields for &#x60;target&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_target_group** | [**List[str]**](str.md)| Limit fields for &#x60;target_group&#x60; resources. If not provided, all fields will be returned | [optional] 
 **include** | [**List[str]**](str.md)| Related associations that will be returned as a flat list of objects. | [optional] 

### Return type

[**GetSubmissionResponse**](GetSubmissionResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bugcrowd.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a &#x60;data&#x60; property containing a submission object. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**400** | An error object indicating unsupported request parameters. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**404** | An error indicating missing resource. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_submissions**
> ListSubmissionsResponse list_submissions(bugcrowd_version=bugcrowd_version, fields_activity=fields_activity, fields_claim_ticket=fields_claim_ticket, fields_comment=fields_comment, fields_cvss_vector=fields_cvss_vector, fields_external_issue=fields_external_issue, fields_file_attachment=fields_file_attachment, fields_identity=fields_identity, fields_monetary_reward=fields_monetary_reward, fields_organization=fields_organization, fields_payment=fields_payment, fields_program=fields_program, fields_program_brief=fields_program_brief, fields_submission=fields_submission, fields_target=fields_target, fields_target_group=fields_target_group, page_limit=page_limit, page_offset=page_offset, include=include, filter_assignee=filter_assignee, filter_blocked_by=filter_blocked_by, filter_duplicate=filter_duplicate, filter_payments=filter_payments, filter_points=filter_points, filter_program=filter_program, filter_researcher=filter_researcher, filter_retest=filter_retest, filter_search=filter_search, filter_severity=filter_severity, filter_source=filter_source, filter_state=filter_state, filter_submitted=filter_submitted, filter_target=filter_target, filter_target_type=filter_target_type, filter_updated=filter_updated, filter_vrt=filter_vrt, sort=sort)

Index submissions

Returns a filtered list of submissions based on tokenized search and sort parameters.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import os
import bugcrowd_client
from bugcrowd_client.models.list_submissions_response import ListSubmissionsResponse
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
    api_instance = bugcrowd_client.SubmissionResourceApi(api_client)
    bugcrowd_version = '{\"$ref\":\"#/info/version\"}'  # str | The request header used to test new API versions before updating the pinned account version (optional)
    fields_activity = [
        'key,submission']  # List[str] | Limit fields for `activity` resources. If not provided, all fields will be returned (optional)
    fields_claim_ticket = [
        'status,claimed_at']  # List[str] | Limit fields for `claim_ticket` resources. If not provided, all fields will be returned (optional)
    fields_comment = [
        'body,author']  # List[str] | Limit fields for `comment` resources. If not provided, all fields will be returned (optional)
    fields_cvss_vector = [
        'version,score']  # List[str] | Limit fields for `cvss_vector` resources. If not provided, all fields will be returned (optional)
    fields_external_issue = [
        'remote_url,remote_id,resource,integration']  # List[str] | Limit fields for `external_issue` resources. If not provided, all fields will be returned (optional)
    fields_file_attachment = [
        'file_name,download_url']  # List[str] | Limit fields for `file_attachment` resources. If not provided, all fields will be returned (optional)
    fields_identity = [
        'name,email']  # List[str] | Limit fields for `identity` resources. If not provided, all fields will be returned (optional)
    fields_monetary_reward = [
        'formatted_amount,cancelled_at']  # List[str] | Limit fields for `monetary_reward` resources. If not provided, all fields will be returned (optional)
    fields_organization = [
        'name,programs']  # List[str] | Limit fields for `organization` resources. If not provided, all fields will be returned (optional)
    fields_payment = [
        'amount_cents,monetary_reward']  # List[str] | Limit fields for `payment` resources. If not provided, all fields will be returned (optional)
    fields_program = [
        'code,organization']  # List[str] | Limit fields for `program` resources. If not provided, all fields will be returned (optional)
    fields_program_brief = [
        'demo,program']  # List[str] | Limit fields for `program_brief` resources. If not provided, all fields will be returned (optional)
    fields_submission = [
        'state,duplicate']  # List[str] | Limit fields for `submission` resources. If not provided, all fields will be returned (optional)
    fields_target = [
        'name,category']  # List[str] | Limit fields for `target` resources. If not provided, all fields will be returned (optional)
    fields_target_group = [
        'name,in_scope']  # List[str] | Limit fields for `target_group` resources. If not provided, all fields will be returned (optional)
    page_limit = 25  # int | Limit parameter for pagination (default page[limit] = 25) (optional) (default to 25)
    page_offset = 0  # int | Offset parameter for pagination (default page[offset] = 0 == first page) (optional) (default to 0)
    include = [
        'program']  # List[str] | Related associations that will be returned as a flat list of objects. (optional)
    filter_assignee = [
        'me,none,user@example.com']  # List[str] | Filter submissions by assignee. Use either an email address or the keywords `me` or `none`  (optional)
    filter_blocked_by = ['filter_blocked_by_example']  # List[str] | Filter submissions by blocked_by (optional)
    filter_duplicate = True  # bool | Filter submissions by duplicate (optional)
    filter_payments = ['filter_payments_example']  # List[str] | Filter submissions by payment information (optional)
    filter_points = ['filter_points_example']  # List[str] | Filter submissions by points (optional)
    filter_program = ['filter_program_example']  # List[str] | Filter submissions by program (optional)
    filter_researcher = ['filter_researcher_example']  # List[str] | Filter submissions by researcher (optional)
    filter_retest = ['filter_retest_example']  # List[str] | Filter submissions by retest (optional)
    filter_search = 'filter_search_example'  # str | Filter submissions by searching through title, description, and comment text (optional)
    filter_severity = [1, 2]  # List[int] | Filter submissions by severity (optional)
    filter_source = ['filter_source_example']  # List[str] | Filter submissions by source (optional)
    filter_state = ['filter_state_example']  # List[str] | Filter submissions by state (optional)
    filter_submitted = '2013-10-20'  # date | Filter submissions by submitted timestamp (optional)
    filter_target = ['filter_target_example']  # List[str] | Filter submissions by target name (optional)
    filter_target_type = ['filter_target_type_example']  # List[str] | Filter submissions by target_type (optional)
    filter_updated = '2013-10-20'  # date | Filter submissions by updated timestamp (optional)
    filter_vrt = 'filter_vrt_example'  # str | Filter submissions by `.` separated vrt id (optional)
    sort = ['submitted-asc,severity-desc']  # List[str] | Tokenized search sort options (optional)

    try:
        # Index submissions
        api_response = api_instance.list_submissions(bugcrowd_version=bugcrowd_version, fields_activity=fields_activity,
                                                     fields_claim_ticket=fields_claim_ticket,
                                                     fields_comment=fields_comment,
                                                     fields_cvss_vector=fields_cvss_vector,
                                                     fields_external_issue=fields_external_issue,
                                                     fields_file_attachment=fields_file_attachment,
                                                     fields_identity=fields_identity,
                                                     fields_monetary_reward=fields_monetary_reward,
                                                     fields_organization=fields_organization,
                                                     fields_payment=fields_payment, fields_program=fields_program,
                                                     fields_program_brief=fields_program_brief,
                                                     fields_submission=fields_submission, fields_target=fields_target,
                                                     fields_target_group=fields_target_group, page_limit=page_limit,
                                                     page_offset=page_offset, include=include,
                                                     filter_assignee=filter_assignee,
                                                     filter_blocked_by=filter_blocked_by,
                                                     filter_duplicate=filter_duplicate, filter_payments=filter_payments,
                                                     filter_points=filter_points, filter_program=filter_program,
                                                     filter_researcher=filter_researcher, filter_retest=filter_retest,
                                                     filter_search=filter_search, filter_severity=filter_severity,
                                                     filter_source=filter_source, filter_state=filter_state,
                                                     filter_submitted=filter_submitted, filter_target=filter_target,
                                                     filter_target_type=filter_target_type,
                                                     filter_updated=filter_updated, filter_vrt=filter_vrt, sort=sort)
        print("The response of SubmissionResourceApi->list_submissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubmissionResourceApi->list_submissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bugcrowd_version** | **str**| The request header used to test new API versions before updating the pinned account version | [optional] 
 **fields_activity** | [**List[str]**](str.md)| Limit fields for &#x60;activity&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_claim_ticket** | [**List[str]**](str.md)| Limit fields for &#x60;claim_ticket&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_comment** | [**List[str]**](str.md)| Limit fields for &#x60;comment&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_cvss_vector** | [**List[str]**](str.md)| Limit fields for &#x60;cvss_vector&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_external_issue** | [**List[str]**](str.md)| Limit fields for &#x60;external_issue&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_file_attachment** | [**List[str]**](str.md)| Limit fields for &#x60;file_attachment&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_identity** | [**List[str]**](str.md)| Limit fields for &#x60;identity&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_monetary_reward** | [**List[str]**](str.md)| Limit fields for &#x60;monetary_reward&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_organization** | [**List[str]**](str.md)| Limit fields for &#x60;organization&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_payment** | [**List[str]**](str.md)| Limit fields for &#x60;payment&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_program** | [**List[str]**](str.md)| Limit fields for &#x60;program&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_program_brief** | [**List[str]**](str.md)| Limit fields for &#x60;program_brief&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_submission** | [**List[str]**](str.md)| Limit fields for &#x60;submission&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_target** | [**List[str]**](str.md)| Limit fields for &#x60;target&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_target_group** | [**List[str]**](str.md)| Limit fields for &#x60;target_group&#x60; resources. If not provided, all fields will be returned | [optional] 
 **page_limit** | **int**| Limit parameter for pagination (default page[limit] &#x3D; 25) | [optional] [default to 25]
 **page_offset** | **int**| Offset parameter for pagination (default page[offset] &#x3D; 0 &#x3D;&#x3D; first page) | [optional] [default to 0]
 **include** | [**List[str]**](str.md)| Related associations that will be returned as a flat list of objects. | [optional] 
 **filter_assignee** | [**List[str]**](str.md)| Filter submissions by assignee. Use either an email address or the keywords &#x60;me&#x60; or &#x60;none&#x60;  | [optional] 
 **filter_blocked_by** | [**List[str]**](str.md)| Filter submissions by blocked_by | [optional] 
 **filter_duplicate** | **bool**| Filter submissions by duplicate | [optional] 
 **filter_payments** | [**List[str]**](str.md)| Filter submissions by payment information | [optional] 
 **filter_points** | [**List[str]**](str.md)| Filter submissions by points | [optional] 
 **filter_program** | [**List[str]**](str.md)| Filter submissions by program | [optional] 
 **filter_researcher** | [**List[str]**](str.md)| Filter submissions by researcher | [optional] 
 **filter_retest** | [**List[str]**](str.md)| Filter submissions by retest | [optional] 
 **filter_search** | **str**| Filter submissions by searching through title, description, and comment text | [optional] 
 **filter_severity** | [**List[int]**](int.md)| Filter submissions by severity | [optional] 
 **filter_source** | [**List[str]**](str.md)| Filter submissions by source | [optional] 
 **filter_state** | [**List[str]**](str.md)| Filter submissions by state | [optional] 
 **filter_submitted** | **date**| Filter submissions by submitted timestamp | [optional] 
 **filter_target** | [**List[str]**](str.md)| Filter submissions by target name | [optional] 
 **filter_target_type** | [**List[str]**](str.md)| Filter submissions by target_type | [optional] 
 **filter_updated** | **date**| Filter submissions by updated timestamp | [optional] 
 **filter_vrt** | **str**| Filter submissions by &#x60;.&#x60; separated vrt id | [optional] 
 **sort** | [**List[str]**](str.md)| Tokenized search sort options | [optional] 

### Return type

[**ListSubmissionsResponse**](ListSubmissionsResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bugcrowd.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a &#x60;data&#x60; property containing an array of submission objects. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**400** | An error object indicating unsupported request parameters. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**404** | An error indicating missing resource. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_submission**
> UpdateSubmissionResponse update_submission(id, update_submission_request, bugcrowd_version=bugcrowd_version)

Update submission

Update a single submission by UUID

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import os
import bugcrowd_client
from bugcrowd_client.models.update_submission_request import UpdateSubmissionRequest
from bugcrowd_client.models.update_submission_response import UpdateSubmissionResponse
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
    api_instance = bugcrowd_client.SubmissionResourceApi(api_client)
    id = '{\"$ref\":\"https://bugcrowd.com/openapi/2024-01-11/external_elements.yml#/general_helpers/ValidUUID\"}'  # str | The ID of the resource in uuid format
    update_submission_request = {"data": {"type": "submission", "attributes": {"severity": 2}, "relationships": {
        "assignee": {"data": {"type": "identity", "id": {
            "$ref": "https://bugcrowd.com/openapi/2024-01-11/external_elements.yml#/general_helpers/ValidUUID"}}}}}}  # UpdateSubmissionRequest | Update a submission
    bugcrowd_version = '{\"$ref\":\"#/info/version\"}'  # str | The request header used to test new API versions before updating the pinned account version (optional)

    try:
        # Update submission
        api_response = api_instance.update_submission(id, update_submission_request, bugcrowd_version=bugcrowd_version)
        print("The response of SubmissionResourceApi->update_submission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubmissionResourceApi->update_submission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource in uuid format | 
 **update_submission_request** | [**UpdateSubmissionRequest**](UpdateSubmissionRequest.md)| Update a submission | 
 **bugcrowd_version** | **str**| The request header used to test new API versions before updating the pinned account version | [optional] 

### Return type

[**UpdateSubmissionResponse**](UpdateSubmissionResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.bugcrowd.v4+json
 - **Accept**: application/vnd.bugcrowd.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a &#x60;data&#x60; property containing updated fields. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**400** | Bad request |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**404** | An error indicating missing resource. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**409** | Incorrect data type parameter |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

