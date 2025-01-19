CTE (common table expression) can be non-recursive or recursive. You can include both of them into your ```WITH``` clause.  

If a recursive CTE is included in WITH clause, the ```RECURSIVE``` keyword must also be included.  

```
WITH RECURSIVE cte_name AS (
  -- Anchor member
  SELECT base_query
  
  UNION ALL
  
  -- Recursive member
  SELECT recursive_query
  FROM cte_name
  WHERE condition
)
SELECT * FROM cte_name;
```

```
with recursive
base1 as (
	(select 1 as n) union all
  (select n * 2 from base1 where n < 10)
)

select * from base1
```

---

```A recursive CTE has reached the maximum number of iterations: 500.```  

---

Multiple subqueries in the same recursive CTE are okay, as long as each recursion has a cycle length of 1.  
![image](https://github.com/user-attachments/assets/08c023db-10d0-4a31-9593-32f33382590f)
