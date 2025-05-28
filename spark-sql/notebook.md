```txt
你在 Notebook 里用 Python 注册的 udf（spark.udf.register），只能在同一个 Notebook/Session 里用，不能拿到 SQL Warehouse 或别的 Notebook 里用；
你在 Databricks SQL Warehouse/SQL 编辑器里，只能用 SQL 级别创建的 Permanent UDF（不支持 Python 写）。
```

## 简单案例  
```py
# 去除特殊字符
from pyspark.sql.types import StringType
import re

def clean_string(s):
    if s is None:
        return None
    # 只保留字母和数字
    return re.sub(r'[^a-zA-Z0-9]', '', s)

spark.udf.register("clean_string", clean_string, StringType())
```

```py
# 字符串转星期几
from pyspark.sql.types import StringType
import datetime

def get_weekday(date_str):
    if date_str is None:
        return None
    d = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return weekday[d.weekday()]

spark.udf.register("get_weekday", get_weekday, StringType())
```

```py
# 判断是否为质数
from pyspark.sql.types import BooleanType
import math

def is_prime(n):
    if n is None or n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

spark.udf.register("is_prime", is_prime, BooleanType())
```

```py
# 条件处理并拼接
from pyspark.sql.types import StringType

def user_status(name, age):
    if age < 18:
        return f"{name} (Minor)"
    else:
        return f"{name} (Adult)"

spark.udf.register("user_status", user_status, StringType())
```

```py
# 
