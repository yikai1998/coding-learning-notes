https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#set_operators  

```select * from Scores```  
```union all``` | ```union distinct``` | ```intersect distinct``` | ```except distinct```  
```select * from Scores2```

```UNION```: Combines rows from two queries, eliminating duplicates (default).  
```ALL```: Includes all duplicates (UNION ALL).  
```DISTINCT```: Removes duplicates (default behavior).  

```INTERSECT```: Returns common rows from both queries.  
```DISTINCT```: Implied; returns distinct common rows.  

```EXCEPT```: Returns rows from the first query that are not in the second query.  
```DISTINCT```: Implied; returns unique rows that are only in the first query.
