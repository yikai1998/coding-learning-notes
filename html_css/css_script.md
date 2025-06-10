# 脚本  
在html中插入脚本 主要用来实现一些动态的页面效果   
type="text/javascript" 这个属性是可选的，因为HTML5中默认的脚本类型就是 text/javascript；可以省略这个属性，代码仍然可以正常工作  
document.write 是一种古老的 JavaScript 方法，用于向浏览器的文档流中直接写内容。虽然在简单的示例中可以使用，但它有一些局限性和潜在问题。现代的 JavaScript 开发中，通常推荐使用更现代的方法来操作 DOM  
<noscript> 标签用于定义在脚本未运行时显示的内容。它通常用于向不支持或禁用了 JavaScript 的用户提供备用内容  
<object> 标签在某些情况下仍然有用，但现代网页设计中更倾向于使用更具体和现代的标签，如 <audio>、<video>、<embed> 和 <iframe>。这些现代标签提供了更好的兼容性和更清晰的语义  
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
