参考链接：https://docs.databricks.com/aws/en/sql/language-manual/data-types  

- ARRAY
  ```sql
  SELECT A.Vaaa[1] FROM VALUES
  (ARRAY(3, 4)),
  (ARRAY(13, 14)),
  (ARRAY(23, 24)) AS A(Vaaa);

  -- 4, 14, 24, each array get the [1]
  ```

- DATE
  ```sql
  select date('2024-12-02 15:00') as create_date;
  ```
  
- DECIMAL
- DOUBLE
- FLOAT
- INT
- INTERVAL
- BIGINT
- BINARY
- BOOLEAN
- VOID
- OBJECT
- SMALLINT
- STRING
- STRUCT
- TIMESTAMP_NTZ
- TINYINT
  
- MAP
  ```sql
  SELECT map('red', 1, 'green', 2);
  
  SELECT m['say'] FROM VALUES(map('say', 'Hello', 'reply', 'World')) AS T(m);
  ```

- TIMESTAMP  
  Timestamps with local timezone are internally normalized and persisted in UTC. Whenever the value or a portion of it is extracted the local session timezone is applied.
  ```sql
  select timestamp('2021-7-1T8:43:28UTC+3')
  -- 2021-07-01T05:43:28.000+00:00
  ```


- VARIANT  
  Represents semi-structured data.
  
