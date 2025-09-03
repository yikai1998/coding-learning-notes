```
UDF
如果仅用 SQL 语法注册，那 UDF 逻辑只能在 Java/Scala 里实现（打成 jar 包，注册到 Spark SQL）
不能用 SQL 写函数体，也不能用 SQL 动态写 Python 函数体
如果你用 Python 写 UDF，只能在 PySpark（Python 程序/Notebook）环境下通过 API 注册，然后在本 session 的 SQL 里用，不能在 SQL Warehouse/SQL 编辑器直接注册，更不能"persist"成全局永久函数。
Databricks、Spark 官方都不支持通过 SQL 写 "Python/Scala/Java" 逻辑函数体；SQL UDF 只能用简单 SQL 语句做些组合。
```


```
建临时视图、写 select 语句，这些 standard SQL 都能用

建持久表（CREATE TABLE）——支持，并写到 catalog/warehouse 里。
建临时视图（CREATE TEMP VIEW）——完全支持，强烈推荐。
CREATE TEMP TABLE —— 语法不推荐／少数 Spark 版本才勉强兼容；优先用 VIEW 替代。
```

```
CREATE OR REPLACE TEMP VIEW t1 AS
SELECT explode(array(struct(10, 20), struct(null, 55))) AS col;

as后的query，不用加分号，也不要最外层括号
CREATE VIEW/CREATE TABLE/CREATE TEMP VIEW 只做定义，没展示结果。
只有 SELECT（或 SHOW TABLES）等查询动作，才会返回内容！
```

```sql
# sample
-- 创建临时人员表
CREATE OR REPLACE TEMP VIEW temp_people AS
SELECT 1 AS id, 'Alice' AS name, DATE('2023-12-01') AS birthday
UNION ALL
SELECT 2, 'Bob', DATE('1995-05-23')
UNION ALL
SELECT 3, 'Cathy', DATE('2000-08-09');

-- 创建临时成绩表
CREATE OR REPLACE TEMP VIEW temp_scores AS
SELECT 1 AS people_id, 80 AS score, DATE('2024-01-01') AS exam_date
UNION ALL
SELECT 1, 90, DATE('2024-03-01')
UNION ALL
SELECT 2, 60, DATE('2024-02-01')
UNION ALL
SELECT 2, 75, DATE('2024-03-05')
UNION ALL
SELECT 3, 92, DATE('2024-03-08');

SELECT
  p.id,
  p.name,
  p.birthday,
  YEAR(current_date()) - YEAR(p.birthday) AS age,
  AVG(s.score) AS avg_score
FROM temp_people p
JOIN temp_scores s
  ON p.id = s.people_id
WHERE s.exam_date >= DATE('2024-01-01')   -- 只看2024年考试
  AND s.score > 70                        -- 分数大于70
GROUP BY p.id, p.name, p.birthday
HAVING AVG(s.score) > 80                  -- 平均分也要大于80
ORDER BY avg_score DESC;
```

```py
把「直接粘来的 id 列表」先变成一个 Python 列表，再用 Notebook 的 参数注入 或 临时视图 两种方式，让后面的 SQL cell 直接当列来用
# 把列表变成 DataFrame
raw = """
id1
id2
id3
id4
"""
ids = [line.strip() for line in raw.strip().splitlines()]
df = spark.createDataFrame([(i, 'hello') for i in ids], "id STRING, temp_str STRING")

# 直接落到永久表或永久视图
df.write.mode("overwrite").option("mergeSchema", "true").saveAsTable("`data-prod-sg`.yikai_test_dbt.tmp_ids")
# 想彻底重建表结构（字段完全保持与 DataFrame 一致）：先Drop，再SaveAsTable 【`spark.sql("DROP TABLE IF EXISTS `data-prod-sg`.yikai_test_dbt.tmp_ids")`】，或用overwriteSchema（若支持）
# 或者：df.createOrReplaceGlobalTempView("tmp_ids") 也可以，但不如落到表简单
```
