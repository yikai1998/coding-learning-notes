# date functions
https://cloud.google.com/bigquery/docs/reference/standard-sql/date_functions  
```CURRENT_DATE```
```
select  
current_date('UTC+8'), # should the current date in location defined by you 
current_date('Asia/Shanghai'), # should the current date in location defined by you 
current_date('+08'), # should the current date in location defined by you 
current_date(), # should the current date of utc by default 
current_date, # should the current date of utc by default 
```

```DATE```
```
SELECT 
DATE(2016, 12, 25) AS date_ymd, # return 2016-12-25 
DATE(DATETIME '2016-12-25 23:59:59') AS date_dt, # return 2016-12-25 
DATE(TIMESTAMP '2016-12-25 22:30:00+08', '+03') AS date_tstz # return 2016-12-25 
# DATE(TIMESTAMP '2016-12-25 22:30:00+08', '+03') firstly tell you 2016-12-25 22:30:00 is in utc+8 location, and return the utc time, finally convert into utc+3 location time 
```

```DATE_ADD```  
```DATE_SUB```  
*Special handling is required for MONTH, QUARTER, and YEAR parts when the date is at (or near) the last day of the month. If the resulting month has fewer days than the original date's day, then the resulting date is the last date of that month.*  

```DATE_DIFF```  
<img width="485" alt="image" src="https://github.com/user-attachments/assets/071b9d60-135b-4673-84a2-d6cc2500f645" />

```DATE_TRUNC```  
```EXTRACT```  
<img width="516" alt="image" src="https://github.com/user-attachments/assets/21541bf2-181c-4d2e-af12-6e09a73a83b6" />
```
SELECT date AS original, DATE_TRUNC(date, WEEK(MONDAY)) AS truncated
FROM (SELECT DATE('2017-11-05') AS date);

/*------------+------------*
 | original   | truncated  |
 +------------+------------+
 | 2017-11-05 | 2017-10-30 |
 *------------+------------*/
```
```
SELECT
  date,
  EXTRACT(ISOYEAR FROM date) AS isoyear,
  EXTRACT(ISOWEEK FROM date) AS isoweek,
  EXTRACT(YEAR FROM date) AS year,
  EXTRACT(WEEK FROM date) AS week
FROM UNNEST(GENERATE_DATE_ARRAY('2015-12-23', '2016-01-09')) AS date
ORDER BY date;

/*------------+---------+---------+------+------*
 | date       | isoyear | isoweek | year | week |
 +------------+---------+---------+------+------+
 | 2015-12-23 | 2015    | 52      | 2015 | 51   |
 | 2015-12-24 | 2015    | 52      | 2015 | 51   |
 | 2015-12-25 | 2015    | 52      | 2015 | 51   |
 | 2015-12-26 | 2015    | 52      | 2015 | 51   |
 | 2015-12-27 | 2015    | 52      | 2015 | 52   |
 | 2015-12-28 | 2015    | 53      | 2015 | 52   |
 | 2015-12-29 | 2015    | 53      | 2015 | 52   |
 | 2015-12-30 | 2015    | 53      | 2015 | 52   |
 | 2015-12-31 | 2015    | 53      | 2015 | 52   |
 | 2016-01-01 | 2015    | 53      | 2016 | 0    |
 | 2016-01-02 | 2015    | 53      | 2016 | 0    |
 | 2016-01-03 | 2015    | 53      | 2016 | 1    |
 | 2016-01-04 | 2016    | 1       | 2016 | 1    |
 | 2016-01-05 | 2016    | 1       | 2016 | 1    |
 | 2016-01-06 | 2016    | 1       | 2016 | 1    |
 | 2016-01-07 | 2016    | 1       | 2016 | 1    |
 | 2016-01-08 | 2016    | 1       | 2016 | 1    |
 | 2016-01-09 | 2016    | 1       | 2016 | 1    |
 *------------+---------+---------+------+------*/
```

```FORMAT_DATE``` 
https://cloud.google.com/bigquery/docs/reference/standard-sql/format-elements#format_elements_date_time  
```FORMAT_DATE(format_string, date_expr)```

```LAST_DAY```  
Returns the last day from a date expression. This is commonly used to return the last day of the month.  

```PARSE_DATE```  
Converts a STRING value to a DATE value.  
```
-- This works because elements on both sides match.
SELECT PARSE_DATE('%A %b %e %Y', 'Thursday Dec 25 2008');

-- This produces an error because the year element is in different locations.
SELECT PARSE_DATE('%Y %A %b %e', 'Thursday Dec 25 2008');

-- This produces an error because one of the year elements is missing.
SELECT PARSE_DATE('%A %b %e', 'Thursday Dec 25 2008');

-- This works because %F can find all matching elements in date_string.
SELECT PARSE_DATE('%F', '2000-12-30');

SELECT PARSE_DATE('%Y%m%d', '20081225') AS parsed;
```
