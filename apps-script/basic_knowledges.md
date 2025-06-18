### `const` | `var` | `let` 在javascript中的区别  
`var` 
1. **作用域**: `var` 在函数作用域内定义变量。如果在函数之外定义，则是全局作用域。`var` 不支持块级作用域。
2. **提升(Hoisting)**: `var` 声明的变量会被提升至作用域顶部，即在代码执行之前变量已存在（但未初始化）。
3. **可重声明**: 在同一作用域内可以多次使用 `var` 声明同一个变量。
4. **可重复赋值**: 将一个新值分配给已经声明的变量

```javascript 
function example() { 
  console.log(foo); // 输出: undefined 
  var foo = 'hello'; 
  console.log(foo); // 输出: 'hello' 
} 
``` 

`let`  
1. **作用域**: `let` 是块级作用域，即它所声明的变量只能在定义它的块中访问。 
2. **提升**: `let` 声明的变量也会被提升，但不会初始化。在变量定义之前访问它们会导致 `ReferenceError`。 
3. **不可重声明**: `let` 在同一作用域内不可重复声明同一个变量。
4. **可重复赋值**: 将一个新值分配给已经声明的变量

```javascript 
if (true) { 
  let bar = 'hi'; 
  console.log(bar); // 输出: 'hi' 
} 

// console.log(bar); // 这行代码会抛出 ReferenceError，因 bar 在块外不可用 
``` 

`const` 
1. **作用域**: 同 `let`，`const` 也是块级作用域。 
2. **常量声明**: `const` 用于声明常量。声明时需要进行初始化，且其绑定的变量引用不可更改（即对基本类型不可重新赋值，对复合类型如对象可修改其属性，但不可重新指向新对象）。 
3. **不可重声明**: `const` 在同一作用域内不可重复声明同一个变量。
4. **不可重复赋值**: 不允许对变量进行重复赋值。声明后，变量的值是不可变的（对于基本数据类型），引用类型的内容可变但引用自身不可重新赋值。 

```javascript 
const baz = 'world'; 
// baz = 'hello'; // 这行代码会导致 TypeError，因为常量不能被重新赋值 

const obj = { key: 'value' }; 
obj.key = 'new value'; // 合法操作，因为我们修改的是对象的属性 
// obj = {}; // 这行代码会导致 TypeError，因为我们试图重新分配一个新对象 
``` 

**其他声明变量的方法**  
除了 `var`、`let` 和 `const`，ES2015（ES6）之后没有新的内置变量声明方式。旧版本 JavaScript 使用 `var` 声明，而现代 JavaScript 开发基本只需使用 `let` 和 `const` 因为它们支持块级作用域和更明显的变量意图声明。  
#### 总结
- **var**: 更宽松，可以重复声明和赋值，但缺乏块级作用域，容易导致意外行为。 
- **let**: 提供块级作用域，无法重复声明，但可重复赋值，是一个灵活且常用的变量声明方式。 
- **const**: 提供块级作用域，不可重复声明或赋值（引用本身不可变，但对象属性和数组项可变），适用于声明不可变的变量。  

因此，`let` 和 `const` 的介绍更多集中在规范性和作用域控制上，而 `var` 是较为宽松的旧式方式，现代 JavaScript 编程更倾向于使用 `let` 和 `const` 来提高代码的可读性和可维护性。 

---

### `map` v.s. `forEach`  
Use `map` when you need to transform each element of an array and create a new array **with** the transformed values.  
```gs
function mapExample() { 
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet(); 
  var range = sheet.getRange("A1:A" + sheet.getLastRow()); 
  var values = range.getValues(); // This returns a 2D array 
  var doubledValues = values.map(function(row) { 
    return [row[0] * 2]; // Multiply the first (and only) element of each sub-array by 2 
  }); 

  // Assume we want to write the doubled values to the second column 
  sheet.getRange(1, 2, doubledValues.length, 1).setValues(doubledValues); 
} 
``` 

Use `forEach` when you need to perform operations on each element of an array **without** creating a new array.  
```gs
function forEachExample() { 
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet(); 
  var range = sheet.getRange("A1:A" + sheet.getLastRow()); 
  var values = range.getValues(); // This returns a 2D array 
  values.forEach(function(row) { 
    Logger.log(row[0]); // Log the first (and only) element of each sub-array 
  }); 
} 
``` 

---

In JavaScript, the three dots (...) represent the spread syntax  
```js
const originalArray = [1, 2, 3];
const copiedArray = [...originalArray]; // [1, 2, 3]

const originalObject = { a: 1, b: 2 };
const copiedObject = { ...originalObject }; // { a: 1, b: 2 }

const numbers = [1, 2];
const newNumbers = [...numbers, 3, 4]; // [1, 2, 3, 4]

function sum(a, b, c) {
    return a + b + c;
}
const args = [1, 2, 3];
const result = sum(...args); // 6
```
