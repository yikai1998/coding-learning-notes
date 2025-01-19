When you use SQL to create arrays, such as with ```ARRAY()``` or ```[]```, you should only include elements of the same data type within the array. This is because SQL arrays are strongly typed, meaning that all elements within an array must conform to the same data type.  
```
SELECT ARRAY[1, 2, 3, 4, 5] AS int_array
```

If you need a collection of mixed-type data, consider structuring your data differently, such as using an array of STRUCTs where each STRUCT can encapsulate multiple fields of different types.  
```
select
  array[
    struct(1 as idx, "alice" as name, true as active),
    struct(2 as idx, "bob" as name, false as active)
  ] as employee
```

---

The ```ARRAY``` constructor is an explicit method to create an array. It is used to specify array elements within an **SQL query**.  
The ```[]``` syntax is often used to provide **array literals directly** in SQL queries. It is shorthand for defining arrays directly.
Regardless of whether you use ARRAY or [], the array elements must be of the same data type within the array.


