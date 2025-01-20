https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#agg_threshold_clause  
```AGGREGATION_THRESHOLD```: This clause ensures that only groups with at least the threshold number of unique privacy_unit_column values are included in the results.  

```
WITH ExamTable AS (
  SELECT "Hansen" AS last_name, "P91" AS test_id, 510 AS test_score UNION ALL
  SELECT "Wang", "U25", 500 UNION ALL
  SELECT "Wang", "C83", 520 UNION ALL
  SELECT "Wang", "U25", 460 UNION ALL
  SELECT "Hansen", "C83", 420 UNION ALL
  SELECT "Hansen", "C83", 560 UNION ALL
  SELECT "Devi", "U25", 580 UNION ALL
  SELECT "Devi", "P91", 480 UNION ALL
  SELECT "Ivanov", "U25", 490 UNION ALL
  SELECT "Ivanov", "P91", 540 UNION ALL
  SELECT "Silva", "U25", 550)
SELECT WITH AGGREGATION_THRESHOLD
  OPTIONS(threshold=3, privacy_unit_column=last_name)
  test_id,
  COUNT(DISTINCT last_name) AS student_count,
  AVG(test_score) AS avg_test_score
FROM ExamTable
GROUP BY test_id;

/*---------+---------------+----------------*
 | test_id | student_count | avg_test_score |
 +---------+---------------+----------------+
 | P91     | 3             | 510.0          |
 | U25     | 4             | 516.0          |
 *---------+---------------+----------------*/
```

```
WITH ExamTable AS (
  SELECT "Hansen" AS last_name, "P91" AS test_id, 510 AS test_score UNION ALL
  SELECT "Wang", "U25", 500 UNION ALL
  SELECT "Wang", "C83", 520 UNION ALL
  SELECT "Wang", "U25", 460 UNION ALL
  SELECT "Hansen", "C83", 420 UNION ALL
  SELECT "Hansen", "C83", 560 UNION ALL
  SELECT "Devi", "U25", 580 UNION ALL
  SELECT "Devi", "P91", 480 UNION ALL
  SELECT "Ivanov", "U25", 490 UNION ALL
  SELECT "Ivanov", "P91", 540 UNION ALL
  SELECT "Silva", "U25", 550)
SELECT
  test_id,
  COUNT(DISTINCT last_name) AS student_count,
  AVG(test_score) AS avg_test_score
FROM ExamTable
GROUP BY test_id;

/*---------+---------------+----------------*
 | test_id | student_count | avg_test_score |
 +---------+---------------+----------------+
 | P91     | 3             | 510.0          |
 | U25     | 4             | 516.0          |
 | C83     | 2             | 500.0          |
 *---------+---------------+----------------*/
```

---

```ANY_VALUE```  
https://cloud.google.com/bigquery/docs/reference/standard-sql/aggregate_functions#any_value  
Returns NULL when the input produces no rows. Returns NULL when expression or expression2 is NULL for all rows in the group.  
```ANY_VALUE``` behaves as if ```IGNORE NULLS``` is specified; rows for which expression is NULL aren't considered and won't be selected.  
If the ```HAVING``` clause is included in the ```ANY_VALUE``` function, the ```OVER``` clause can't be used with this function.  
```
SELECT
  fruit,
  ANY_VALUE(fruit) OVER (ORDER BY LENGTH(fruit) ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS any_value
FROM UNNEST(["apple", "banana", "pear"]) as fruit;

/*--------+-----------*
 | fruit  | any_value |
 +--------+-----------+
 | pear   | pear      |
 | apple  | pear      |
 | banana | apple     |
 *--------+-----------*/
```
```
WITH
  Store AS (
    SELECT 20 AS sold, "apples" AS fruit
    UNION ALL
    SELECT 30 AS sold, "pears" AS fruit
    UNION ALL
    SELECT 30 AS sold, "bananas" AS fruit
    UNION ALL
    SELECT 10 AS sold, "oranges" AS fruit
  )
SELECT ANY_VALUE(fruit HAVING MAX sold) AS a_highest_selling_fruit FROM Store;

/*-------------------------*
 | a_highest_selling_fruit |
 +-------------------------+
 | pears                   |
 *-------------------------*/
```
```
WITH
  Store AS (
    SELECT 20 AS sold, "apples" AS fruit, 'benny' AS name
    UNION ALL
    SELECT 30 AS sold, "pears" AS fruit, 'tom'
    UNION ALL
    SELECT 30 AS sold, "bananas" AS fruit, 'alice'
    UNION ALL
    SELECT 10 AS sold, "oranges" AS fruit, 'kitty'
  )
SELECT ANY_VALUE([fruit, name] HAVING MIN LENGTH(name)) AS a_highest_selling_fruit FROM Store;

/*-------------------------*
 | a_highest_selling_fruit |
 +-------------------------+
 | pears                   |
 | tom                     |
 *-------------------------*/
```

---

```ARRAY_AGG```
https://cloud.google.com/bigquery/docs/reference/standard-sql/aggregate_functions#array_agg  
如果你使用```ARRAY_AGG()```作为聚合函数，可以使用 GROUP BY。 
如果你使用```ARRAY_AGG()```作为窗口函数（通过```OVER```子句），则不能使用```GROUP BY```，因为窗口函数的逻辑是基于每一行的。 
If this function is used with the OVER clause, it's part of a window function call. In a window function call, aggregate function clauses can't be used.  
```
WITH vals AS
  (
    SELECT 1 x UNION ALL
    SELECT -2 x UNION ALL
    SELECT 3 x UNION ALL
    SELECT -2 x UNION ALL
    SELECT 1 x
  )
SELECT ARRAY_AGG(DISTINCT x ORDER BY x) as array_agg
FROM vals;

/*------------*
 | array_agg  |
 +------------+
 | [-2, 1, 3] |
 *------------*/
```

---

```ARRAY_CONCAT_AGG```
https://cloud.google.com/bigquery/docs/reference/standard-sql/aggregate_functions#array_concat_agg  
Concatenates elements from expression of type ARRAY, returning a single array as a result.
```
SELECT FORMAT("%T", ARRAY_CONCAT_AGG(x ORDER BY ARRAY_LENGTH(x))) AS array_concat_agg FROM (
  SELECT [1, 2, 3, 4, NULL] AS x
  UNION ALL SELECT [5, 6]
  UNION ALL SELECT [7, 8, 9]
);

/*-----------------------------------*
 | array_concat_agg                  |
 +-----------------------------------+
 | [5, 6, 7, 8, 9, 1, 2, 3, 4, NULL] |
 *-----------------------------------*/
```
%T 是 FORMAT 函数中的一个占位符，用于将数组或结构体以结构化的字符串形式输出。 

---

```AVG```  

```COUNT```  

```COUNT(DISTINCT ...)``` will ignore the NULL values, so it will count only the distinct values of expression for which condition is TRUE.
```
SELECT COUNT(DISTINCT CASE WHEN x > 0 THEN x WHEN x < 0 THEN -1*x ELSE NULL END) AS distinct_positive
FROM UNNEST([1, -2, 4, 1, -5, 4, 1, 3, -6, 1]) AS x;
```

```COUNTIF```  
Since expression must be a BOOL, the form ```COUNTIF(DISTINCT ...)``` is generally not useful: there is only one distinct value of TRUE. So ```COUNTIF(DISTINCT ...)``` will return 1 if expression evaluates to TRUE for one or more input rows, or 0 otherwise.
Usually when someone wants to combine ```COUNTIF``` and ```DISTINCT```, they want to count the number of distinct values of an expression for which a certain condition is satisfied. One recipe to achieve this is the following:  
```COUNT(DISTINCT IF(condition, expression, NULL))```

```GROUPING```  
https://cloud.google.com/bigquery/docs/reference/standard-sql/aggregate_functions#grouping  
If a groupable item in the GROUP BY clause is aggregated (and thus not grouped), this function returns 1. Otherwise, this function returns 0.  

```LOGICAL_AND```  
```LOGICAL_OR```
```
SELECT LOGICAL_AND(x < 3) AS logical_and FROM UNNEST([1, 2, 4]) AS x;

/*-------------*
 | logical_and |
 +-------------+
 | FALSE       |
 *-------------*/
```

```MAX```  
```MIN```
```MAX_BY```  
```MIN_BY```  
Synonym for ```ANY_VALUE(x HAVING MAX y)```  
Synonym for ```ANY_VALUE(x HAVING MIN y)```  
```
WITH fruits AS (
  SELECT "apple"  fruit, 3.55 price UNION ALL
  SELECT "banana"  fruit, 2.10 price UNION ALL
  SELECT "pear"  fruit, 4.30 price
)
SELECT MIN_BY(fruit, price) as fruit
FROM fruits;

/*--------*
 | fruit  |
 +--------+
 | banana |
 *--------*/
```

```STRING_AGG```
https://cloud.google.com/bigquery/docs/reference/standard-sql/aggregate_functions#string_agg  
Returns a value (either STRING or BYTES) obtained by concatenating non-NULL values. Returns NULL if there are zero input rows or expression evaluates to NULL for all rows.  
```
SELECT STRING_AGG(DISTINCT fruit, " & " ORDER BY fruit) AS string_agg
FROM UNNEST(["apple", "pear", "banana", "pear", NULL]) AS fruit;

/*-----------------------*
 | string_agg            |
 +-----------------------+
 | apple & banana & pear |
 *-----------------------*/
```
