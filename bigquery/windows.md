https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#window_clause  
3 different ways you can combine named windows and use them in a window function's ```OVER``` clause, they all return the same results.  
the WINDOW clause defines a reusable window specification.  

```
SELECT
  item,
  purchases,
  category,
  LAST_VALUE(item) OVER (item_window) AS most_popular 
FROM Produce 

WINDOW item_window AS ( 
  PARTITION BY category 
  ORDER BY purchases 
  ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING
)
```

```
SELECT
  item,
  purchases,
  category,
  LAST_VALUE(item) OVER (d) AS most_popular 
FROM Produce 

WINDOW
  a AS (PARTITION BY category), 
  b AS (a ORDER BY purchases), 
  c AS (b ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING), 
  d AS (c) 
```

```
SELECT
  item, purchases,
  category,
  LAST_VALUE(item) OVER (c ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING) AS most_popular 
FROM Produce 

WINDOW 
  a AS (PARTITION BY category), 
  b AS (a ORDER BY purchases), 
  c AS b 
```

---

#### What is the use of ```ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING```?  
*In BigQuery, the ```ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING``` clause is actually the default window frame specification for many window functions when combined with ```PARTITION BY``` and sometimes ```ORDER BY```.  
The implicit frame is ```ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING``` unless an ```ORDER BY``` clause is present, which changes the default frame to ```RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW```*  

---

#### ```NTH_VALUE()``` vs. ```FIRST_VALUE```
*They essentially do the same thing when applied over the same window.*  

---

#### ```PERCENTILE_CONT``` vs. ```PERCENTILE_DISC``` 

```PERCENTILE_CONT``` (percentile continuous) computes the percentile value as a continuous distribution. This means:
- It interpolates between values to compute the requested percentile, which can result in a value that might not actually exist in the dataset. 
- This is particularly useful when you need a more precise measure of the percentile that accounts for the entire range of values, not just the discrete values you have.  
  
```PERCENTILE_DISC``` (percentile discrete) calculates the percentile value based on discrete rank without interpolation. This means: 
- It returns the actual value from the dataset that represents the percentile, without calculating a value in between the dataset values. 
- This is useful when you need an actual member of your dataset to represent the percentile, often used in business scenarios or categorical data. 

---

https://cloud.google.com/bigquery/docs/reference/standard-sql/window-function-calls#compute_a_grand_total  
Compute grand total  
```
SELECT 
  item, 
  purchases, 
  category, 
  SUM(purchases) OVER () AS total_purchases 
FROM Produce
```
  
https://cloud.google.com/bigquery/docs/reference/standard-sql/window-function-calls#compute_a_subtotal  
Compute sub total 
```
SELECT
  item,
  purchases,
  category,
  SUM(purchases) OVER (PARTITION BY category ORDER BY purchases ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS total_purchases 
FROM Produce 
```
   
https://cloud.google.com/bigquery/docs/reference/standard-sql/window-function-calls#compute_a_cumulative_sum  
Compute cumulative sum 
```
SELECT
  item,
  purchases,
  category,
  SUM(purchases) OVER (PARTITION BY category ORDER BY purchases ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS total_purchases
  # You don't have to add CURRENT ROW as a boundary unless you would like to for readability. 
FROM Produce 
```
  
https://cloud.google.com/bigquery/docs/reference/standard-sql/window-function-calls#compute_a_moving_average  
Compute moving average 
```
SELECT
  item,
  purchases,
  category,
  AVG(purchases) OVER (PARTITION BY category ORDER BY purchases ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS avg_purchases
FROM Produce 
```

---

https://cloud.google.com/bigquery/docs/reference/standard-sql/window-function-calls#compute_the_number_of_items_within_a_range  
Compute the number of items within a range 
```
SELECT
  animal,
  population,
  category,
  COUNT(*) OVER (ORDER BY population RANGE BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS similar_population 
FROM Farm; 
```
In SQL window functions, the ```RANGE``` frame specification allows you to compute aggregates based on a range of values relative to the current row within the sorted partition. Specifically, it can refer to a set of rows that precede and follow the current row based on a specified range of values in the ORDER BY clause.  
```RANGE``` uses the first ```ORDER BY``` column to define numerical range boundaries.  
  
```ROWS``` clause: Only considers a fixed number of rows regardless of the values.   
```RANGE``` clause: Considers all rows within the specified value range. This is particularly useful for dealing with continuous values like timestamps, where you want to consider a range around the row's value, not just a fixed count of preceding and following rows.  
  
The ```RANGE``` clause syntax adapts based on the type of the ordering column: 
- Numeric Columns: No INTERVAL required.  
- Date/Time Columns: Typically use INTERVAL for defining frames in time units.
<img width="551" alt="image" src="https://github.com/user-attachments/assets/7d94b1e1-c8d4-4716-9c8c-35b3b1cc7934" />

---

https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#qualify_clause  
<img width="606" alt="image" src="https://github.com/user-attachments/assets/40a99137-467b-4e13-a94e-0ed977a82df3" />
