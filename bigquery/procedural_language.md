https://cloud.google.com/bigquery/docs/reference/standard-sql/procedural-language  
The GoogleSQL procedural language lets you execute multiple statements in one query as a multi-statement query. You can use a multi-statement query to:  
1. Run multiple statements in a sequence, with shared state. 
2. Automate management tasks such as creating or dropping tables. 
3. Implement complex logic using programming constructs such as IF and WHILE.

---

```DECLARE```
Declares a variable of the specified type. If the ```DEFAULT``` clause is specified, the variable is initialized with the value of the expression; if no ```DEFAULT``` clause is present, the variable is initialized with the value NULL.  
Variable declarations must appear before other procedural statements, or at the start of a ```BEGIN``` block. Variable names are case-insensitive. 
```
DECLARE x INT64; DECLARE y INT64;  
DECLARE d DATE DEFAULT CURRENT_DATE(); 
DECLARE x, y, z INT64 DEFAULT 0; [The following example initializes the variables x, y, and z as INT64 with the value 0.] 
DECLARE item DEFAULT (SELECT item FROM schema1.products LIMIT 1); 
```

---

```BEGIN``` initiates a block of statements where declared variables exist only until the corresponding ```END```  
```
DECLARE x INT64 DEFAULT 10; 
BEGIN 
  DECLARE y INT64; 
  SET y = x; 
  SELECT x, y; 
END; 
SELECT x; 
# SELECT x, y; Query error: Unrecognized name: y at [8:11]
```
```BEGIN...EXCEPTION``` executes a block of statements. If any of the statements encounter an error, the remainder of the block is skipped and the statements in the ```EXCEPTION``` clause are executed.  
```
BEGIN 
  SELECT 10/0 AS a; 
EXCEPTION WHEN ERROR THEN 
  SELECT  
    100 AS a, 
    @@error.message, # Specifies a human-readable error message 
    @@error.stack_trace, # Each element of the array corresponds to a statement or procedure call executing at the time of the error, with the currently executing stack frame appearing first 
    @@error.statement_text, # Specifies the text of the statement which caused the error 
    @@error.formatted_stack_trace; # The content of @@error.stack_trace expressed as a human readable string. This value is intended for display purposes, and is subject to change without notice. Programmatic access to an error's stack trace should use @@error.stack_trace instead 
END; 
```

---

```CASE```  
```
DECLARE target_product_id INT64 DEFAULT 103;
CASE
  WHEN
    103 > target_product_id
    THEN SELECT '103 > target_product_id';
  WHEN
    103 = target_product_id
    THEN SELECT '103 = target_product_id';
  ELSE
    SELECT 'what?';
END CASE;
```

---

```IF```  
```
IF condition THEN [sql_statement_list] 

  [ELSEIF condition THEN sql_statement_list] 

  [...] 

  [ELSE sql_statement_list] 

END IF;
```

---

```LOOP```  
Executes sql_statement_list until a ```BREAK``` or ```LEAVE``` statement exits the loop. sql_statement_list is a list of zero or more SQL statements ending with semicolons.  
```
# 执行一次select，但里面的内容有迭代🔁
DECLARE x INT64 DEFAULT 0; 
LOOP 
  SET x = x + 1; 
  IF x >= 10 THEN LEAVE; END IF; 
END LOOP; 

SELECT x;
```
```
# 重复执行多次select
DECLARE x INT64 DEFAULT 0; 
REPEAT 
  SET x = x + 1; 
  SELECT x; 
  UNTIL x >= 3 
END REPEAT; 
```
