# swagger_client.GeneApi

All URIs are relative to *https://www.phenopolis.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gene_get**](GeneApi.md#gene_get) | **GET** /gene | 


# **gene_get**
> list[Gene] gene_get(id, gnomad_freq=gnomad_freq, cadd=cadd)



Get gene by id but also filter variants out by CADD and freq

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
api_instance = swagger_client.GeneApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Gene ENSEMBL id
gnomad_freq = 8.14 # float | gnomad allele freq threshold (optional)
cadd = 8.14 # float | CADD threshold (optional)

try:
    # 
    api_response = api_instance.gene_get(id, gnomad_freq=gnomad_freq, cadd=cadd)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneApi->gene_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Gene ENSEMBL id | 
 **gnomad_freq** | **float**| gnomad allele freq threshold | [optional] 
 **cadd** | **float**| CADD threshold | [optional] 

### Return type

[**list[Gene]**](Gene.md)

### Authorization

[phenopolis_auth](../README.md#phenopolis_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

