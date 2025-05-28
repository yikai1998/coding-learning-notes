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
