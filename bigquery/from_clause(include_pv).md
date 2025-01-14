how to get some samples from a table <br>
```select * from `bigquery-public-data.usa_names.usa_1910_2013` tablesample system (10 percent)```

---
add the ```pivot/unpivot``` after ```from``` <br>

PIVOT operator - rotates rows into columns, using aggregation
```
-- 创建示例数据表
WITH sales AS (
  SELECT 1 AS sale_id, 'Product A' AS product_name, '2024-01-01' AS sale_date, 10 AS quantity_sold UNION ALL
  SELECT 2, 'Product B', '2024-01-01', 15 UNION ALL
  SELECT 3, 'Product C', '2024-01-01', 20 UNION ALL
  SELECT 4, 'Product A', '2024-01-02', 12 UNION ALL
  SELECT 5, 'Product B', '2024-01-02', 18 UNION ALL
  SELECT 6, 'Product C', '2024-01-02', 22
)
-- 使用PIVOT子句进行查询
SELECT *
FROM (
  SELECT sale_date, product_name, quantity_sold
  FROM sales
)
PIVOT (
  SUM(quantity_sold) FOR product_name IN ('Product A' AS product_a, 'Product B' AS product_b, 'Product C' AS product_c)
)
ORDER BY sale_date;
```
![image](https://github.com/user-attachments/assets/c88e7e8a-f6cd-4c2e-80ec-b5d2486e641f)

<br>UNPIVOT operator - rotates columns into rows

```
-- 创建示例数据表
WITH sales_pivot AS (
  SELECT '2024-01-01' AS sale_date, 10 AS `Product A`, 15 AS `Product B`, 20 AS `Product C` UNION ALL
  SELECT '2024-01-02', 12, 18, 22
)
-- 使用UNPIVOT子句进行查询
SELECT sale_date, product_name, quantity_sold
FROM (
  SELECT sale_date, `Product A`, `Product B`, `Product C`
  FROM sales_pivot
)
UNPIVOT (
  quantity_sold FOR product_name IN (`Product A` AS 'product_a', `Product B` AS 'product_b', `Product C` AS 'product_c')
)
ORDER BY sale_date, product_name;
```
![image](https://github.com/user-attachments/assets/f2c828c1-a79b-4bd4-b8f8-78b50fd7ddea)

<br> UNPIVOT operator with multiple columns

```
-- 创建示例数据表
WITH sales_pivot AS (
  SELECT '2024-01-01' AS sale_date, 10 AS `Product A`, 15 AS `Product B`, 20 AS `Product C`, 90 AS `Product D` UNION ALL
  SELECT '2024-01-02', 12, 18, 22, 50
)
-- 使用UNPIVOT子句进行查询
SELECT sale_date, product_name, quantity_sold, quantity_sold2
FROM (
  SELECT sale_date, `Product A`, `Product B`, `Product C`, `Product D`
  FROM sales_pivot
)
UNPIVOT (
  (quantity_sold, quantity_sold2) FOR product_name IN ((`Product A`,`Product B`) AS 'product_ab', (`Product C`, `Product D`) AS 'product_cd')
)
ORDER BY sale_date, product_name;
```
![image](https://github.com/user-attachments/assets/9b48d28f-27b3-4fa6-b414-51e19c6f3b38)
![image](https://github.com/user-attachments/assets/9351511a-2931-4335-adcf-fdee90e15d75)
