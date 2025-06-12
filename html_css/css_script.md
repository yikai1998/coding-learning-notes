# 脚本  
在html中插入脚本 主要用来实现一些动态的页面效果   
type="text/javascript" 这个属性是可选的，因为HTML5中默认的脚本类型就是 text/javascript；可以省略这个属性，代码仍然可以正常工作  
document.write 是一种古老的 JavaScript 方法，用于向浏览器的文档流中直接写内容。虽然在简单的示例中可以使用，但它有一些局限性和潜在问题。现代的 JavaScript 开发中，通常推荐使用更现代的方法来操作 DOM  
`<noscript>` 标签用于定义在脚本未运行时显示的内容。它通常用于向不支持或禁用了 JavaScript 的用户提供备用内容  
`<object>` 标签在某些情况下仍然有用，但现代网页设计中更倾向于使用更具体和现代的标签，如 `<audio>、<video>、<embed> 和 <iframe>`。这些现代标签提供了更好的兼容性和更清晰的语义  
```html
    <div id="msg"></div>
    <script>document.getElementById("msg").textContent = "你个傻逼"</script>
```
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        /* 设置 #output 元素的样式，包括上边距、内边距、边框和最小高度 */
        #output {
            margin-top: 20px;
            padding: 10px;
            border: 1px solid black;
            min-height: 50px;
        }
    </style>
</head>
<body>
    <h1>Interactive Form with Color Picker</h1>
    <form id="inputForm">
        <label for="userInput">Enter some text:</label>
        <input type="text" id="userInput" required>
        <label for="colorSelect">Choose a color:</label>
        <input type="color" id="colorSelect">
        <label for="fontSelect">Choose a font:</label>
        <select id="fontSelect">
            <option value="Arial">Arial</option>
            <option value="Times New Roman">Times New Roman</option>
            <option value="Courier New">Courier New</option>
            <option value="华文正楷">华文正楷</option>
            <option value="Cooper Black">Cooper Black</option>
        </select>
        <label for="styleSelect">Choose a style:</label>
        <select id="styleSelect">
            <option value="normal">Normal</option>
            <option value="bold">Bold</option>
            <option value="italic">Italic</option>
            <option value="underline">Underline</option>
        </select>
        <button type="button" onclick="submitForm()">Submit</button>  <!-- 提交按钮，点击时调用 submitForm 函数 -->
    </form>
    <div id="output"></div>  <!-- 输出区域，用于显示用户输入的文本 -->

    <script>
        function submitForm() {
            const userInput = document.getElementById('userInput').value;  // 获取文本输入框的值
            const colorSelect = document.getElementById('colorSelect').value;  // 获取颜色选择器的值
            const fontSelect = document.getElementById('fontSelect').value;  // 获取字体选择器的值
            const styleSelect = document.getElementById('styleSelect').value;  // 获取样式选择器的值
            const divOutput = document.getElementById('output');  // 获取输出区域的元素

            divOutput.textContent = '';  // 清空输出区域的元素
            const paragraph = document.createElement('p');  // 创建一个新的段落元素
            paragraph.textContent = userInput;  // 设置该段落的文本内容为输入框的值
            paragraph.style.color = colorSelect;  // 设置该段落的文本颜色为颜色选择器的值
            paragraph.style.fontFamily = fontSelect;  // 设置该段落的字体为字体选择器的值
            // 根据样式选择器的值设置样式
            switch (styleSelect) {
                case 'bold':
                    paragraph.style.fontWeight = 'bold';
                    break;
                case 'italic':
                    paragraph.style.fontStyle = 'italic';
                    break;
                case 'underline':
                    paragraph.style.textDecoration = 'underline';
                    break;
                default:
                    // 如果 styleSelect 的值不匹配任何 case，则执行 default 分支，将字体样式设置为默认值
                    paragraph.style.fontWeight = 'normal';
                    paragraph.style.fontStyle = 'normal';
                    paragraph.style.textDecoration = 'none';
            }
            divOutput.appendChild(paragraph);  // 将段落添加到输出区域
        }
    </script>
    <noscript>没执行</noscript>  <!-- <noscript> 标签的内容是 "没执行"，但你没有看到这个内容，原因可能是你的浏览器启用了 JavaScript。当 JavaScript 被启用时，浏览器会忽略 <noscript> 标签中的内容 -->
</body>
</html>
```

---

## event  
`addEventListener` 可以替代传统的内联事件处理器（如 onclick、ondblclick、onmousemove、onkeydown 等）。`addEventListener` 提供了更多的控制力和灵活性，是现代Web开发中推荐的事件处理方式。  
为什么使用 addEventListener
- 支持多个事件处理器：你可以为同一个元素的同一个事件类型添加多个处理程序，而不会相互覆盖。例如，你可以为一个按钮同时添加多个点击事件处理器。
- 代码分离：将HTML代码和JavaScript代码分离，使代码更易于维护和管理。例如，你可以在一个单独的JavaScript文件中处理所有事件，而不是在HTML标签中直接绑定事件。
- 更好的控制力：你可以指定事件的捕获阶段（capture 参数），控制事件的传播。例如，你可以决定事件是在捕获阶段还是冒泡阶段被处理。

```js
document.getElementById('submitButton').addEventListener('click', submitForm);
```
```txt
click：鼠标点击事件。
dblclick：鼠标双击事件。
mouseover：鼠标移入事件。
mouseout：鼠标移出事件。
mousemove：鼠标移动事件。
mousedown：鼠标按下事件。
mouseup：鼠标释放事件。
keydown：按键按下事件。event.key 属性返回一个字符串，表示被按下的键的值。
keyup：按键释放事件。
...
```
```js
// 为窗口添加键盘事件处理器
        window.addEventListener('keydown', function(event) {
            outputDiv.textContent = `Key pressed: ${event.key}`;
        });

// 为窗口添加 contextmenu 事件处理器
        window.addEventListener('contextmenu', function(event) {
            event.preventDefault(); // 阻止默认的上下文菜单
            outputDiv.textContent = 'You right-clicked at (' + event.clientX + ', ' + event.clientY + ')';
        });
```
