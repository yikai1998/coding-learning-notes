https://cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax  
The BigQuery data manipulation language (DML) enables you to update, insert, and delete data from your BigQuery tables.  

---

```Partition Table``` v.s. ```Non-Partition Table```  

#### Partition Table  
A partition table is a database table that has been divided into smaller, more manageable pieces called partitions. Each partition is stored separately, but all partitions are treated as a single logical table in queries. Partitioning can significantly improve performance, manageability, and availability of large datasets. Here are the main types of partitioning:  
1. Range Partitioning: Divides data based on a specified range of values.  
Example: Partitioning a sales table based on a date column so that each partition represents one month of sales data.  
2. List Partitioning: Divides data based on a list of values.  
Example: Partitioning a customer table based on regions such as North, South, East, and West.  
3. Hash Partitioning: Distributes data across partitions using a hash function.  
Example: Evenly distributing customer records across multiple partitions using a hash of the customer ID.  
4. Composite Partitioning: Combines multiple partitioning strategies.  
Example: Applying range partitioning first and then hash partitioning within each range.  

##### Benefits of Partition Tables:  
Performance: Queries that target specific data can run faster because they can access only the partitions they need.  
Manageability: Operations like backups and archiving can be performed on individual partitions rather than the entire table.  
Scalability: Helps in distributing the data across multiple storage devices.  

##### Non-Partition Table:  
Stores data as a single logical unit.  
Simpler administration but may not scale well with very large datasets.  

---

Use the ```INSERT``` statement when you want to add new rows to a table.   
```
# using explicit values 
INSERT dataset.DetailedInventory 
VALUES 
('top load washer', 10, FALSE, [(CURRENT_DATE, "comment1")], ("white", "1 year", (30,40,28))),
('front load washer', 20, FALSE, [(CURRENT_DATE, "comment1")], ("beige", "1 year", (35,45,30)))

# select statement
INSERT dataset.Warehouse (warehouse, state)
WITH w AS (
  SELECT ARRAY<STRUCT<warehouse string, state string>>
      [('warehouse #1', 'WA'),
       ('warehouse #2', 'CA'),
       ('warehouse #3', 'WA')] col
)
SELECT warehouse, state FROM w, UNNEST(w.col)

# one of the values is computed using a subquery
INSERT dataset.DetailedInventory (product, quantity)
VALUES('countertop microwave',
  (SELECT quantity FROM dataset.DetailedInventory
   WHERE product = 'microwave'))
```

---

Use the ```DELETE``` statement when you want to delete rows from a table.  
Each time you construct a ```DELETE``` statement, you must use the ```WHERE``` keyword, followed by a condition. The ```WHERE``` keyword is mandatory for any ```DELETE``` statement.  
```
DELETE dataset.Inventory i 
WHERE i.product NOT IN (SELECT product from dataset.NewArrivals)
```

---

Use the ```TRUNCATE``` TABLE statement, to delete all rows in a table.  
The ```TRUNCATE``` TABLE statement removes all rows from a table but leaves the table metadata intact, including the table schema, description, and labels. 
*A table schema in a database defines the structure of the table. It consists of the table name and the details about its columns, including their names, data types, constraints, and other attributes. This schema dictates how the data is stored and accessed within the table.*  
*Metrics in this context reflect properties and operational characteristics of database tables. These include size, number of rows, last refresh times, and more.*  
```
TRUNCATE TABLE [[project_name.]dataset_name.]table_name 
```

---

Use the ```UPDATE``` statement when you want to update existing rows within a table.  
```
UPDATE dataset.Inventory 
SET quantity = quantity - 10, 
    supply_constrained = DEFAULT 
WHERE product like '%washer%' 
```
```
UPDATE dataset.Inventory 
SET quantity = quantity + (SELECT quantity FROM dataset.NewArrivals 
  WHERE Inventory.product = NewArrivals.product), 
    supply_constrained = false 
  WHERE product IN (SELECT product FROM dataset.NewArrivals) 
```
```
UPDATE dataset.Inventory i 
SET quantity = i.quantity + n.quantity, 
    supply_constrained = false 
FROM dataset.NewArrivals n 
WHERE i.product = n.product 
```
```
UPDATE dataset.DetailedInventory 
SET specifications.color = 'white', 
    specifications.warranty = '1 year' 
WHERE product like '%washer%' 
```

---

A ```MERGE``` statement is a DML statement that can combine ```INSERT, UPDATE, and DELETE``` operations into a single statement and perform the operations atomically.  
```
MERGE dataset.Inventory T 
USING dataset.NewArrivals S ON T.product = S.product 
WHEN MATCHED THEN UPDATE SET quantity = T.quantity + S.quantity 
WHEN NOT MATCHED THEN INSERT (product, quantity) VALUES(product, quantity) 
```

---

<img width="733" alt="image" src="https://github.com/user-attachments/assets/eace2589-8f9b-48f4-aaf3-5617723d24b7" />
