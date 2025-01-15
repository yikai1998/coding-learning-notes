The ```USING``` clause in SQL, including BigQuery, offers a more concise and readable way to specify join conditions, but it comes with some limitations compared to the ```ON``` clause as it is only useful when the columns used in the join condition have the same name in both tables.  

---

```CROSS JOIN``` can be written implicitly with a comma. This is called a comma cross join.  
```CROSS JOIN``` does not use a join condition; it combines each row from the first table with each row from the second table.  

---
https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#full_join  
```FULL OUTER JOIN``` (or simply ```FULL JOIN```) returns all fields for all matching rows in both from_items that meet the join condition. If a given row from one from_item doesn't join to any row in the other from_item, the row returns with NULL values for all columns from the other from_item.  

---

While you are using a similar ```FROM ... , UNNEST(...)``` structure in both queries, ***the second query does not exhibit a traditional CROSS JOIN effect. Instead, it utilizes a correlated (or implicit) join to expand nested arrays.***
