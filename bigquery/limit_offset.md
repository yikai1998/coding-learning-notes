you need both ```LIMIT``` and ```OFFSET``` to use OFFSET effectively, as OFFSET cannot generally be used by itself
however, ```LIMIT``` could be used independently.  

By specifying a very large number for LIMIT, you can mimic the behavior of using OFFSET alone, effectively skipping a certain number of rows and then returning the rest of the rows from the query.
