https://cloud.google.com/bigquery/docs/reference/standard-sql/conversion_functions#cast  
```CAST``` syntax is used in a query to indicate that the result type of an expression should be converted to some other type.  
When using ```CAST```, a query can fail if GoogleSQL is unable to perform the cast. If you want to protect your queries from these types of errors, you can use ```SAFE_CAST```  



Some casts can include a format clause, which provides instructions for how to conduct the cast.  
https://cloud.google.com/bigquery/docs/reference/standard-sql/format-elements#formatting_syntax   
```
SELECT CAST('06/02/2020 17:00:53.110' AS TIMESTAMP FORMAT 'MM/DD/YYYY HH24:MI:SS.FF3' AT TIME ZONE 'UTC+8') AS as_timestamp
# 2020-06-02 09:00:53.110000 UTC
```  
这里的format指的是 如何解读cast of source info，at time zone同理




