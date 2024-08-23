# PaginatedResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**size** | **int** |  | 
**items** | [**List[DataProduct]**](DataProduct.md) |  | 

## Example

```python
from ds_connector.models.paginated_result import PaginatedResult

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResult from a JSON string
paginated_result_instance = PaginatedResult.from_json(json)
# print the JSON string representation of the object
print PaginatedResult.to_json()

# convert the object into a dict
paginated_result_dict = paginated_result_instance.to_dict()
# create an instance of PaginatedResult from a dict
paginated_result_form_dict = paginated_result.from_dict(paginated_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


