# swagger-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: phenopolis_auth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# create an instance of the API class
api_instance = swagger_client.GeneApi()
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

## Documentation for API Endpoints

All URIs are relative to *https://www.phenopolis.org/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*GeneApi* | [**gene_get**](docs/GeneApi.md#gene_get) | **GET** /gene | 
*PatientApi* | [**patient_get**](docs/PatientApi.md#patient_get) | **GET** /patient | Returns patient
*PhenotypeApi* | [**hpo_get**](docs/PhenotypeApi.md#hpo_get) | **GET** /hpo/ | Returns Human Phenotype Ontology (HPO)
*VariantApi* | [**find_variants_by_id**](docs/VariantApi.md#find_variants_by_id) | **GET** /variant | Finds Variants by id
*VariantApi* | [**get_variant_by_id**](docs/VariantApi.md#get_variant_by_id) | **GET** /variant/{variantId} | Find variant by ID


## Documentation For Models

 - [Gene](docs/Gene.md)
 - [HPO](docs/HPO.md)
 - [Patient](docs/Patient.md)
 - [SimpleVariant](docs/SimpleVariant.md)
 - [Variant](docs/Variant.md)
 - [VariantCarriers](docs/VariantCarriers.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: HTTP header

## phenopolis_auth

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: https://www.phenopolis.org/oauth/dialog
- **Scopes**: 
 - **write:variants**: modify variants in your account
 - **read:variants**: read your variants


## Author

info@phenopolis.org
