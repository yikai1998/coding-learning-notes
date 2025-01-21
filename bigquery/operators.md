#### Array subscript operator  
```OFFSET(index)```: The index starts at zero. Produces an error if the index is out of range. To produce NULL instead of an error, use SAFE_OFFSET(index). This position keyword produces the same result as index by itself.  
```SAFE_OFFSET(index)```: The index starts at zero. Returns NULL if the index is out of range.  
```ORDINAL(index)```: The index starts at one. Produces an error if the index is out of range. To produce NULL instead of an error, use SAFE_ORDINAL(index).  
```SAFE_ORDINAL(index)```: The index starts at one. Returns NULL if the index is out of range.  
![image](https://github.com/user-attachments/assets/a9cdd2b7-cfc0-4cb5-8619-08a51d574614)

#### JSON subscript operator
Gets a value of an array element or field in a JSON expression. Can be used to access nested data.  
![image](https://github.com/user-attachments/assets/3726b3e5-28f6-4ae6-b909-e98f176c1730)

#### Date arithmetics operators  
This is equivalent to DATE_ADD or DATE_SUB functions, when interval is expressed in days.  
```
SELECT DATE "2020-09-22" + 1 AS day_later, DATE "2020-09-22" - 7 AS week_ago
```

#### Datetime subtraction  
```
SELECT
  DATE "2021-05-20" - DATE "2020-04-19" AS date_diff,
  TIMESTAMP "2021-06-01 12:34:56.789" - TIMESTAMP "2021-05-31 00:00:00" AS time_diff
```
```
SELECT
  DATE "2021-04-20" + INTERVAL 25 HOUR AS date_plus,
  TIMESTAMP "2021-05-02 00:01:02.345" - INTERVAL 10 SECOND AS time_minus;
```

#### Comparison operators  
The result of ```X BETWEEN Y AND Z``` is equivalent to ```Y <= X AND X <= Z```  

#### ```EXISTS``` operator  
Returns TRUE if the subquery produces one or more rows.   

#### ```IN``` operator  
```
search_value [NOT] IN value_set

value_set:
  {
    (expression[, ...])
    | (subquery)
    | UNNEST(array_expression)
  }
```

#### ```LIKE``` operator  
A percent sign ```%``` matches any number of characters or bytes.
An underscore ```_``` matches a single character or byte.
You can escape ```\``` ```_``` ```%``` using two backslashes. For example, ```\\%```. If you are using raw strings, only a single backslash is required. For example, ```r'\%'```
