# swagger_client.VariantApi

All URIs are relative to *https://www.phenopolis.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_variants_by_id**](VariantApi.md#find_variants_by_id) | **GET** /variant | Finds Variants by id
[**get_variant_by_id**](VariantApi.md#get_variant_by_id) | **GET** /variant/{variantId} | Find variant by ID


# **find_variants_by_id**
> list[Variant] find_variants_by_id(id)

Finds Variants by id

Multiple variant ids can be provided with comma separated strings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: phenopolis_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.VariantApi(swagger_client.ApiClient(configuration))
id = ['id_example'] # list[str] | 

try:
    # Finds Variants by id
    api_response = api_instance.find_variants_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariantApi->find_variants_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)|  | 

### Return type

[**list[Variant]**](Variant.md)

### Authorization

[phenopolis_auth](../README.md#phenopolis_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variant_by_id**
> Variant get_variant_by_id(variant_id)

Find variant by ID

Returns a single variant

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
api_instance = swagger_client.VariantApi(swagger_client.ApiClient(configuration))
variant_id = 789 # int | ID of variant to return

try:
    # Find variant by ID
    api_response = api_instance.get_variant_by_id(variant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariantApi->get_variant_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variant_id** | **int**| ID of variant to return | 

### Return type

[**Variant**](Variant.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

