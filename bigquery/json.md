```JSON_QUERY```  
```JSON_QUERY_ARRAY```  
https://cloud.google.com/bigquery/docs/reference/standard-sql/json_functions#json_extract   
```
SELECT JSON_QUERY('{"a": [123, 689], "b": [["hello", "hello2"], "world"]}', '$.b[0]');  # string ["hello","hello2"]
SELECT JSON_QUERY_ARRAY('{"a": [123, 689], "b": [["hello", "hello2"], "world"]}', '$.b[0]');  # array ["hello","hello2"]
```

```JSON_VALUE```  
Extracts a JSON scalar value and converts it to a SQL STRING value. In addition, this function removes the outermost quotes and unescapes the values.  
```
SELECT JSON_VALUE('{"a": [123, 689], "b": [["hello", "hello2"], "world"]}', '$.a[1]');
SELECT JSON_QUERY_ARRAY('{"a": [[123, 689]], "b": [["hello", "hello2"], "world"]}', '$.a[0]');
```

```JSON_KEYS```  
Extracts unique JSON keys from a JSON expression.  
```
SELECT JSON_KEYS( 
  JSON '{"a":[{"b":1}, {"c":2}], "d":3}', 
  mode => "lax") as json_keys
```
<img width="473" alt="image" src="https://github.com/user-attachments/assets/9841929f-5fac-445d-93df-3daa07e887e9" />  

```JSON_REMOVE```  
https://cloud.google.com/bigquery/docs/reference/standard-sql/json_functions#json_remove  
Produces a new SQL JSON value with the specified JSON data removed.  
In the following example, path ```$.a.b``` and ```$.b``` don't exist, so those operations are ignored, but the others are processed.  
```
SELECT JSON_REMOVE(JSON '{"a": [1, 2, 3]}', '$.a[0]', '$.a.b', '$.b', '$.a[0]') AS json_data

/*-----------*
 | json_data |
 +-----------+
 | {"a":[3]} |
 *-----------*/
```

```JASON_SET```  
Produces a new SQL JSON value with the specified JSON data inserted or replaced.  
https://cloud.google.com/bigquery/docs/reference/standard-sql/json_functions#json_set  
```
# In the following example, the path $.a.c implies that the value at $.a is a JSON object but it's not.
# This part of the operation is ignored, but the other parts of the operation are completed successfully.
SELECT JSON_SET(
  JSON '{"a": 1}',
  '$.b', 2,
  '$.a.c', 100,
  '$.d', 3, create_if_missing => true) AS json_data

/*---------------------*
 | json_data           |
 +---------------------+
 | {"a":1,"b":2,"d":3} |
 *---------------------*/
```
```
SELECT JSON_SET(
  JSON '{"a": 1}',
  '$.b', 2,
  '$.a.c', 100,
  '$.d', 3, create_if_missing => false) AS json_data

/*---------------------*
 | json_data           |
 +---------------------+
 | {"a":1}             |
 *---------------------*/
```
```
SELECT JSON_SET(
  JSON '{"a": {"idx": 0}}',
  '$.b', 2,
  '$.a.c', 100,
  '$.d', 3, create_if_missing => true) AS json_data

/*-------------------------------------*
 | json_data                           |
 +-------------------------------------+
 | {"a":{"c":100,"idx":0},"b":2,"d":3} |
 *------------------------------------*/
```

https://cloud.google.com/bigquery/docs/reference/standard-sql/json_functions#parse_json  
```PARSE_JSON``` Converts a JSON-formatted STRING value to a JSON value.  
```TO_JSON``` Converts a SQL value to a JSON value.   
```TO_JSON_STRING``` Converts a SQL value to a JSON-formatted STRING value. 
