参考链接：https://spark.apache.org/docs/latest/sql-ref-functions-builtin.html  

# 主要是一些基本常见的函数整理  

## array related
- array_append(array, element)  // Add the element at the end of the array. Type of element should be similar to type of the elements of the array.
- array_prepend
- array_compact(array)  // Removes null values from the array.
- array_contains(array, value)  // Returns true if the array contains the value.
- array_distinct(array)  // Removes duplicate values from the array.
- array_except(array1, array2)  // Returns an array of the elements in array1 but not in array2, without duplicates.
- array_insert(x, pos, val)  // Places val into index pos of array x. Array indices start at 1. The maximum negative index is -1 for which the function inserts new element after the current last element.
- array_intersect(array1, array2)  // Returns an array of the elements in the intersection of array1 and array2, without duplicates.
- arrays_overlap  // Returns true if a1 contains at least a non-null element present also in a2. If the arrays have no common element and they are both non-empty and either of them contains a null element null is returned, false otherwise.
- array_join(array, delimiter[, nullReplacement])	 // Concatenates the elements of the given array using the delimiter and an optional string to replace nulls. If no value is set for nullReplacement, any null value is filtered.
```sql
SELECT array_join(array('hello', null ,'world'), ' ', ',');
```
- array_min, array_max, array_postion (1-based, 0 if not found)
- array_remove  // Remove all elements that equal to element from array.
- array_repeat  // Returns the array containing element count times.
```sql
SELECT array_repeat('123', 2);
```
- array_union  // Returns an array of the elements in the union of array1 and array2, without duplicates.
- arrays_zip  // Returns a merged array of structs in which the N-th struct contains all N-th values of input arrays.
```sql
SELECT arrays_zip(array(1, 2, 3), array(2, 3, 4));  -- [{1, 2}, {2, 3}]
SELECT arrays_zip(array(1, 2), array(2, 3), array(3, 4));  -- [{1, 2, 3}, {2, 3, 4}]
```
- flatten  // Transforms an array of arrays into a single array.
```sql
SELECT flatten(array(array(1, 2), array(3, 4)));  -- [1, 2, 3, 4]
```
- get(array, index)	 // Returns element of array at given (0-based) index. If the index points outside of the array boundaries, then this function returns NULL.
- sequence(start, stop, step)
- slice(x, start, length)	 // Subsets array x starting from index start (array indices start at 1, or starting from the end if start is negative) with the specified length.
- sort_array(array[, ascendingOrder])	 // Null elements will be placed at the beginning of the returned array in ascending order or at the end of the returned array in descending order.
- 
