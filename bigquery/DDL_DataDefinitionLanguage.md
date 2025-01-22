### Data definition language (DDL)  
https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language  

---

```CREATE TABLE```  
```
CREATE [ OR REPLACE ] [ TEMP | TEMPORARY ] TABLE [ IF NOT EXISTS ]
table_name
[(
  column | constraint_definition[, ...]
)]
[DEFAULT COLLATE collate_specification]
[PARTITION BY partition_expression]
[CLUSTER BY clustering_column_list]
[WITH CONNECTION connection_name]
[OPTIONS(table_option_list)]
[AS query_statement]

column:=
column_definition

constraint_definition:=
[primary_key]
| [[CONSTRAINT constraint_name] foreign_key, ...]

primary_key :=
PRIMARY KEY (column_name[, ...]) NOT ENFORCED

foreign_key :=
FOREIGN KEY (column_name[, ...]) foreign_reference

foreign_reference :=
REFERENCES primary_key_table(column_name[, ...]) NOT ENFORCED
```

```
CREATE TEMP TABLE tmp_table (column_number INT64, column_string STRING);  

INSERT INTO tmp_table(column_number, column_string) 
VALUES(11, 'test'),(22, 'test2'); 

SELECT * FROM tmp_table;
```

The ```INSERT INTO``` and ```INSERT``` statements in SQL can sometimes be a source of confusion, but they are essentially the same thing—both are used to insert new data into a table.  
Modern SQL standards and most RDBMS (Relational Database Management Systems) prefer or require the INSERT INTO syntax.  

---

```CREATE FUNCTION```  
Creates a new user-defined function (UDF). BigQuery supports UDFs written in either SQL or JavaScript.  
You can define UDFs as either persistent or temporary. You can reuse persistent UDFs across multiple queries, while temporary UDFs only exist in the scope of a single query.  
```
CREATE TEMP FUNCTION AddFourAndDivide(x INT64, y INT64) RETURNS FLOAT64 
AS ( 
  (x + 4) / y 
); 
CREATE TEMP FUNCTION lastArrayElement(arr ANY TYPE) RETURNS FLOAT64
AS ( 
  arr[ORDINAL(ARRAY_LENGTH(arr))] 
); 
CREATE TEMP FUNCTION ConvertToIntArray(arr ARRAY<STRING>) RETURNS ARRAY<INT64>
AS (
  ARRAY(SELECT CAST(x AS INT64) FROM UNNEST(arr) AS x)
);


SELECT 
  val, 
  AddFourAndDivide(val, 2) 
FROM 
  UNNEST([2,3,5,8]) AS val; 

SELECT 
  lastArrayElement(x) AS last_element 
FROM ( 
  SELECT [2,3,5,8,13.9] AS x
); 

SELECT ConvertToIntArray(['1', '2', '3']) AS result;
```

 
