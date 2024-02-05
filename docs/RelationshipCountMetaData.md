# RelationshipCountMetaData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**total_hits** | **int** |  | 

## Example

```python
from bugcrowd_client.models.relationship_count_meta_data import RelationshipCountMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipCountMetaData from a JSON string
relationship_count_meta_data_instance = RelationshipCountMetaData.from_json(json)
# print the JSON string representation of the object
print
RelationshipCountMetaData.to_json()

# convert the object into a dict
relationship_count_meta_data_dict = relationship_count_meta_data_instance.to_dict()
# create an instance of RelationshipCountMetaData from a dict
relationship_count_meta_data_form_dict = relationship_count_meta_data.from_dict(relationship_count_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


