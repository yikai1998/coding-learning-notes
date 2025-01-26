```SELECT DISTINCT``` cannot return columns of the following types: ```STRUCT``` ```ARRAY```

struct() is to make all fields with in the parenthesis into one json

array is to make the whole select result into one row

---
```SELECT AS STRUCT```
This produces a value table with a STRUCT row type, where the STRUCT field names and types match the column names and types produced in the SELECT list.
select as struct is to make all columns behind the select into one json

---
sample <br>
```SELECT AS STRUCT 1 a, 2 b``` <br>
![image](https://github.com/user-attachments/assets/24621af8-ef8d-4b63-ba3b-57179e7949a3)

```SELECT ARRAY(SELECT AS STRUCT 1 a, 2 b) AS a_array``` <br>
![image](https://github.com/user-attachments/assets/4e7a8b31-edee-415d-af43-397730de904d)


![image](https://github.com/user-attachments/assets/794464fc-cc1a-4c0f-8892-ed11e18c7420)

---

```SELECT * REPLACE```  
Note: SELECT * REPLACE doesn't replace columns that don't have names.  
```
WITH orders AS
  (SELECT 5 as order_id,
  "sprocket" as item_name,
  200 as quantity)
SELECT * REPLACE ("widget" AS item_name)
FROM orders;

/*----------+-----------+----------*
 | order_id | item_name | quantity |
 +----------+-----------+----------+
 | 5        | widget    | 200      |
 *----------+-----------+----------*/

WITH orders AS
  (SELECT 5 as order_id,
  "sprocket" as item_name,
  200 as quantity)
SELECT * REPLACE (quantity/2 AS quantity)
FROM orders;

/*----------+-----------+----------*
 | order_id | item_name | quantity |
 +----------+-----------+----------+
 | 5        | sprocket  | 100      |
 *----------+-----------+----------*/
```
