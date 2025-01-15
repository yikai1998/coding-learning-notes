https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#group_by_all  
The ```GROUP BY ALL``` clause groups rows by inferring grouping keys from the SELECT items.  

---
https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#group_by_grouping_sets  
GROUP BY GROUPING SETS(x,y) is roughly equivalent to GROUP BY x UNION ALL GROUP BY y  
```
-- GROUP BY with GROUPING SETS
WITH
  Products AS (
    SELECT 'shirt' AS product_type, 't-shirt' AS product_name, 3 AS product_count UNION ALL
    SELECT 'shirt', 't-shirt', 8 UNION ALL
    SELECT 'shirt', 'polo', 25 UNION ALL
    SELECT 'pants', 'jeans', 6
  )
SELECT product_type, product_name, SUM(product_count) AS product_sum
FROM Products
GROUP BY GROUPING SETS (product_type, product_name)
ORDER BY product_name

/*--------------+--------------+-------------+
 | product_type | product_name | product_sum |
 +--------------+--------------+-------------+
 | shirt        | NULL         | 36          |
 | pants        | NULL         | 6           |
 | NULL         | jeans        | 6           |
 | NULL         | polo         | 25          |
 | NULL         | t-shirt      | 11          |
 +--------------+--------------+-------------*/
```
