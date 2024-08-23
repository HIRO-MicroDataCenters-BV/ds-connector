# ds_connector.DataProductApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_product**](DataProductApi.md#get_data_product) | **GET** /data-products/{connector_id}/{data_product_id}/ | Get a data product details
[**get_data_products**](DataProductApi.md#get_data_products) | **GET** /data-products/ | Get a list of data products


# **get_data_product**
> DataProduct get_data_product(connector_id, data_product_id)

Get a data product details

Returns an information about the data product

### Example


```python
import ds_connector
from ds_connector.models.data_product import DataProduct
from ds_connector.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ds_connector.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ds_connector.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ds_connector.DataProductApi(api_client)
    connector_id = 'connector_id_example' # str | 
    data_product_id = 'data_product_id_example' # str | 

    try:
        # Get a data product details
        api_response = api_instance.get_data_product(connector_id, data_product_id)
        print("The response of DataProductApi->get_data_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataProductApi->get_data_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 
 **data_product_id** | **str**|  | 

### Return type

[**DataProduct**](DataProduct.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_products**
> PaginatedResult get_data_products(page=page, page_size=page_size)

Get a list of data products

Returns a list of data products with the ability to paginate

### Example


```python
import ds_connector
from ds_connector.models.paginated_result import PaginatedResult
from ds_connector.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ds_connector.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ds_connector.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ds_connector.DataProductApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 100 # int |  (optional) (default to 100)

    try:
        # Get a list of data products
        api_response = api_instance.get_data_products(page=page, page_size=page_size)
        print("The response of DataProductApi->get_data_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataProductApi->get_data_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 100]

### Return type

[**PaginatedResult**](PaginatedResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

