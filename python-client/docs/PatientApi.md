# swagger_client.PatientApi

All URIs are relative to *https://www.phenopolis.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patient_get**](PatientApi.md#patient_get) | **GET** /patient | Returns patient


# **patient_get**
> Patient patient_get()

Returns patient



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PatientApi(swagger_client.ApiClient(configuration))

try:
    # Returns patient
    api_response = api_instance.patient_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PatientApi->patient_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Patient**](Patient.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

