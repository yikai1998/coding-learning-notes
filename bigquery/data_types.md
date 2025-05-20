## [data types](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types)  

---

`Numeric` types include the following types:
`INT64` with alias INT, SMALLINT, INTEGER, BIGINT, TINYINT, BYTEINT  
`NUMERIC` with alias DECIMAL  
`BIGNUMERIC` with alias BIGDECIMAL  
`FLOAT64`  

float和numeric的对比  
<img width="748" alt="image" src="https://github.com/user-attachments/assets/03ae93e9-f556-4bdd-94eb-a99df6bd3b17" />

```
struct 就是把一组字段合成一个对象（结构体/行）
array 就是一组数值打包成队列（数组/列表）
map 就是一组key-value对组成的字典
unnest 就是把这些包起来的东西拆开变多行
```
