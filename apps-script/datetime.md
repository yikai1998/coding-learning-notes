### basic sample
```gs
function getFormattedCurrentDateTime() { 
  var now = new Date(); 
  var timeZone = Session.getScriptTimeZone(); // Get the script's timezone, or specify your own as 'GMT+8' 
  var formattedDate = Utilities.formatDate(now, timeZone, 'yyyy-MM-dd'); 
  var formattedDateTime = Utilities.formatDate(now, 'GMT+8', 'yyyy-MM-dd HH:mm:ss'); 

  Logger.log(formattedDate)
  Logger.log(formattedDateTime)
} 
```
```gs
  today = [today.getFullYear(), (today.getMonth()+1).toString().padStart(2, '0'), (today.getDate()).toString().padStart(2, '0')].join('-')
```

```
yyyy: Four-digit year. 
yy: Two-digit year. 
MMM: Abbreviated month name. 
MMMM: Full month name. 
MM: Two-digit month (01-12). 
dd: Two-digit day of the month (01-31). 
HH: Two-digit hour in 24-hour format (00-23). 
hh: Two-digit hour in 12-hour format (01-12). 
mm: Two-digit minutes (00-59). 
ss: Two-digit seconds (00-59). 
a: AM/PM marker. // 'HH:mm:ss a' formats the current time in HH:MM:SS AM/PM format. 
u: Represents the day number of the week with Monday as day 1 through to Sunday as day 7. 
```

the `Utilities.formatDate` method outputs the date or time as a string.  

---

### some common ways to create Date objects
```gs
var now = new Date(); // Current date and time 
var specificDate = new Date(2023, 8, 5); // Note: Months are 0-based (January = 0, December = 11) //September 5, 2023 
var specificDateTime = new Date(2023, 8, 5, 14, 30, 0); // September 5, 2023 14:30:00 
var dateFromTimestamp = new Date(1672531199000); // Unix timestamp in milliseconds 
var dateFromString = new Date("2023-09-05T14:30:00Z"); // ISO-8601 format
```

---

### For non-standard date strings, you will need to parse the string manually, for example: 
```gs
var dateString = "05-September-2023"; 
var parts = dateString.split("-"); 
var day = parseInt(parts[0], 10); 
var month = new Date(Date.parse(parts[1] +" 1, 2012")).getMonth(); 
var year = parseInt(parts[2], 10); 
var dateFromString = new Date(year, month, day); 
```
<img width="572" alt="image" src="https://github.com/user-attachments/assets/219dd91b-c532-457d-94dc-95f8c7c4af20" />

---

you can directly subtract one Date object from another, and JavaScript will automatically convert the dates to milliseconds to perform the calculation.  
When you modify the minutes of a Date object using the setMinutes method, JavaScript automatically handles the overflow for you. This means that if the total minutes exceed 60, it will correctly increment the hours and set the minutes to the correct remainder.  
```gs
function differenceInDays(date1, date2) { 
  var diffTime = Math.abs(date2 - date1); 
  var diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)); 

  return diffDays;
} 
```
```gs
var anotherDate = new Date(); 
anotherDate.setDate(anotherDate.getDate() + 10); // 10 days in the future 
var daysDifference = differenceInDays(today, anotherDate); 
Logger.log('Difference in Days: ' + daysDifference); 
```
similar as month, ... calculation
```gs
var now = new Date()
var year = now.getFullYear()
var lastMonth = now.getMonth() - 1
var lastMonthDate = new Date(year, lastMonth, 1)
var lastMonth = Utilities.formatDate(lastMonthDate, 'GMT+8', 'yyyyMM')
```
