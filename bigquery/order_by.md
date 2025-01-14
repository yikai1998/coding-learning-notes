https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#order_by_clause

```
SELECT 
x, y
FROM (
  SELECT 1 AS x, TRUE AS y UNION ALL
  SELECT 9, TRUE UNION ALL
  SELECT NULL, FALSE
)
ORDER BY x DESC NULLS FIRST;
```

fyi  
![image](https://github.com/user-attachments/assets/055688ce-b8c2-48ae-b449-2e1e3faac6ae)
