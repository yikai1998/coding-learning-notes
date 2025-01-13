```SELECT DISTINCT``` cannot return columns of the following types: ```STRUCT``` ```ARRAY```

struct() is to make all fields with in the parenthesis into one json

array is to make the whole select result into one row

---
```SELECT AS STRUCT```
This produces a value table with a STRUCT row type, where the STRUCT field names and types match the column names and types produced in the SELECT list.

```SELECT ARRAY(SELECT AS STRUCT 1 a, 2 b)```
select as struct is to make all columns behind the select into one json

sample
![image](https://github.com/user-attachments/assets/794464fc-cc1a-4c0f-8892-ed11e18c7420)


