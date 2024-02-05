# bugcrowd_client.MonetaryRewardResourceApi

All URIs are relative to *https://api.bugcrowd.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_monetary_reward**](MonetaryRewardResourceApi.md#create_monetary_reward) | **POST** /monetary_rewards | Create reward
[**get_monetary_reward**](MonetaryRewardResourceApi.md#get_monetary_reward) | **GET** /monetary_rewards/{id} | Fetch reward
[**update_monetary_reward**](MonetaryRewardResourceApi.md#update_monetary_reward) | **PATCH** /monetary_rewards/{id} | Update reward


# **create_monetary_reward**
> CreateMonetaryRewardResponse create_monetary_reward(create_monetary_reward_request)

Create reward

Create a new monetary reward for a submission.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import os
import bugcrowd_client
from bugcrowd_client.models.create_monetary_reward_request import CreateMonetaryRewardRequest
from bugcrowd_client.models.create_monetary_reward_response import CreateMonetaryRewardResponse
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
    api_instance = bugcrowd_client.MonetaryRewardResourceApi(api_client)
    create_monetary_reward_request = {"data": {"type": "monetary_reward", "attributes": {"amount_cents": 1000},
                                               "relationships": {"submission": {"data": {"type": "submission", "id": {
                                                   "$ref": "https://bugcrowd.com/openapi/2024-01-11/external_elements.yml#/general_helpers/ValidUUID"}}}}}}  # CreateMonetaryRewardRequest | A monetary reward resource with a submission relationship.

    try:
        # Create reward
        api_response = api_instance.create_monetary_reward(create_monetary_reward_request)
        print("The response of MonetaryRewardResourceApi->create_monetary_reward:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonetaryRewardResourceApi->create_monetary_reward: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_monetary_reward_request** | [**CreateMonetaryRewardRequest**](CreateMonetaryRewardRequest.md)| A monetary reward resource with a submission relationship. | 

### Return type

[**CreateMonetaryRewardResponse**](CreateMonetaryRewardResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.bugcrowd.v4+json
 - **Accept**: application/vnd.bugcrowd.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Monetary reward created |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**400** | Bad request |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**403** | Forbidden client-generated ID |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**404** | An error indicating missing resource. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**409** | Incorrect data type parameter |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**422** | Record failed to validate, operation rolled back |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monetary_reward**
> GetMonetaryRewardResponse get_monetary_reward(id, bugcrowd_version=bugcrowd_version, fields_identity=fields_identity, fields_monetary_reward=fields_monetary_reward, fields_payment=fields_payment, fields_submission=fields_submission, include=include)

Fetch reward

Returns a single monetary reward by UUID.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import os
import bugcrowd_client
from bugcrowd_client.models.get_monetary_reward_response import GetMonetaryRewardResponse
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
    api_instance = bugcrowd_client.MonetaryRewardResourceApi(api_client)
    id = '{\"$ref\":\"https://bugcrowd.com/openapi/2024-01-11/external_elements.yml#/general_helpers/ValidUUID\"}'  # str | The ID of the resource in uuid format
    bugcrowd_version = '{\"$ref\":\"#/info/version\"}'  # str | The request header used to test new API versions before updating the pinned account version (optional)
    fields_identity = [
        'name,email']  # List[str] | Limit fields for `identity` resources. If not provided, all fields will be returned (optional)
    fields_monetary_reward = [
        'formatted_amount,cancelled_at']  # List[str] | Limit fields for `monetary_reward` resources. If not provided, all fields will be returned (optional)
    fields_payment = [
        'amount_cents,monetary_reward']  # List[str] | Limit fields for `payment` resources. If not provided, all fields will be returned (optional)
    fields_submission = [
        'state,duplicate']  # List[str] | Limit fields for `submission` resources. If not provided, all fields will be returned (optional)
    include = [
        'rewarded_by']  # List[str] | Related associations that will be returned as a flat list of objects. (optional)

    try:
        # Fetch reward
        api_response = api_instance.get_monetary_reward(id, bugcrowd_version=bugcrowd_version,
                                                        fields_identity=fields_identity,
                                                        fields_monetary_reward=fields_monetary_reward,
                                                        fields_payment=fields_payment,
                                                        fields_submission=fields_submission, include=include)
        print("The response of MonetaryRewardResourceApi->get_monetary_reward:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonetaryRewardResourceApi->get_monetary_reward: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource in uuid format | 
 **bugcrowd_version** | **str**| The request header used to test new API versions before updating the pinned account version | [optional] 
 **fields_identity** | [**List[str]**](str.md)| Limit fields for &#x60;identity&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_monetary_reward** | [**List[str]**](str.md)| Limit fields for &#x60;monetary_reward&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_payment** | [**List[str]**](str.md)| Limit fields for &#x60;payment&#x60; resources. If not provided, all fields will be returned | [optional] 
 **fields_submission** | [**List[str]**](str.md)| Limit fields for &#x60;submission&#x60; resources. If not provided, all fields will be returned | [optional] 
 **include** | [**List[str]**](str.md)| Related associations that will be returned as a flat list of objects. | [optional] 

### Return type

[**GetMonetaryRewardResponse**](GetMonetaryRewardResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bugcrowd.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a &#x60;data&#x60; property containing a monetary_reward object. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**400** | An error object indicating unsupported request parameters. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**404** | An error indicating missing resource. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_monetary_reward**
> UpdateMonetaryRewardResponse update_monetary_reward(id, update_monetary_reward_request, bugcrowd_version=bugcrowd_version)

Update reward

Cancel a monetary reward and provide a reason

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import os
import bugcrowd_client
from bugcrowd_client.models.update_monetary_reward_request import UpdateMonetaryRewardRequest
from bugcrowd_client.models.update_monetary_reward_response import UpdateMonetaryRewardResponse
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
    api_instance = bugcrowd_client.MonetaryRewardResourceApi(api_client)
    id = '{\"$ref\":\"https://bugcrowd.com/openapi/2024-01-11/external_elements.yml#/general_helpers/ValidUUID\"}'  # str | The ID of the resource in uuid format
    update_monetary_reward_request = {"data": {"type": "monetary_reward", "attributes": {"cancelled": true,
                                                                                         "cancellation_reason": "other"}}}  # UpdateMonetaryRewardRequest | Update reward
    bugcrowd_version = '{\"$ref\":\"#/info/version\"}'  # str | The request header used to test new API versions before updating the pinned account version (optional)

    try:
        # Update reward
        api_response = api_instance.update_monetary_reward(id, update_monetary_reward_request,
                                                           bugcrowd_version=bugcrowd_version)
        print("The response of MonetaryRewardResourceApi->update_monetary_reward:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonetaryRewardResourceApi->update_monetary_reward: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource in uuid format | 
 **update_monetary_reward_request** | [**UpdateMonetaryRewardRequest**](UpdateMonetaryRewardRequest.md)| Update reward | 
 **bugcrowd_version** | **str**| The request header used to test new API versions before updating the pinned account version | [optional] 

### Return type

[**UpdateMonetaryRewardResponse**](UpdateMonetaryRewardResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.bugcrowd.v4+json
 - **Accept**: application/vnd.bugcrowd.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Monetary reward updated |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**400** | An error in the request body |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**404** | An error indicating missing resource. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**422** | Invalid attribute options |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

