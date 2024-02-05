# bugcrowd_client.ClaimTicketResourceApi

All URIs are relative to *https://api.bugcrowd.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_claim_ticket**](ClaimTicketResourceApi.md#create_claim_ticket) | **POST** /claim_tickets | Create claim ticket


# **create_claim_ticket**
> CreateClaimTicketResponse create_claim_ticket(create_claim_ticket_request)

Create claim ticket

Create claim ticket with submission relationship.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import os
import bugcrowd_client
from bugcrowd_client.models.create_claim_ticket_request import CreateClaimTicketRequest
from bugcrowd_client.models.create_claim_ticket_response import CreateClaimTicketResponse
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
    api_instance = bugcrowd_client.ClaimTicketResourceApi(api_client)
    create_claim_ticket_request = {"data": {"type": "claim_ticket", "relationships": {"submissions": {"data": [
        {"type": "submission", "id": {
            "$ref": "https://bugcrowd.com/openapi/2024-01-11/external_elements.yml#/general_helpers/ValidUUID"}}]}}}}  # CreateClaimTicketRequest | 

    try:
        # Create claim ticket
        api_response = api_instance.create_claim_ticket(create_claim_ticket_request)
        print("The response of ClaimTicketResourceApi->create_claim_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClaimTicketResourceApi->create_claim_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_claim_ticket_request** | [**CreateClaimTicketRequest**](CreateClaimTicketRequest.md)|  | 

### Return type

[**CreateClaimTicketResponse**](CreateClaimTicketResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.bugcrowd.v4+json
 - **Accept**: application/vnd.bugcrowd.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Claim ticket created |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**400** | Bad request |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**403** | Forbidden client-generated ID |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**404** | An error indicating missing resource. |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |
**409** | Incorrect data type parameter |  * X-Bugcrowd-Media-Type -  <br>  * X-Bugcrowd-Version -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

