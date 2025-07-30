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

---

```
/* 1. 建表 */
CREATE TEMP TABLE emp (
    id        INT64,
    name      STRING,
    leader_id INT64
);

/* 2. 测试数据（3 棵树：1-CEO、9-副总X、14-副总Y） */
INSERT INTO emp (id, name, leader_id) VALUES
-- 第 1 棵树（CEO 旗下）
( 1, 'CEO'      , NULL),
( 2, 'Alice'    , 1),
( 3, 'Bob'      , 1),
( 4, 'Charlie'  , 2),
( 5, 'David'    , 2),
( 6, 'Eva'      , 3),
( 7, 'Frank'    , 4),
( 8, 'Grace'    , 6),

-- 第 2 棵树（副总X 旗下）
( 9, '副总X'    , NULL),
(10, 'Helen'    , 9),
(11, 'Ivy'      , 9),
(12, 'Jack'     ,11),

-- 第 3 棵树（副总Y 旗下）
(14, '副总Y'    , NULL),
(15, 'Kevin'    ,14);

WITH RECURSIVE r AS (
    SELECT id, name, id AS top_leader_id
    FROM   emp
    WHERE  leader_id IS NULL
    
    UNION ALL
    
    SELECT e.id, e.name, r.top_leader_id
    FROM   emp e
    JOIN   r ON e.leader_id = r.id
)
SELECT id, name, top_leader_id
FROM   r
ORDER  BY id;
```
