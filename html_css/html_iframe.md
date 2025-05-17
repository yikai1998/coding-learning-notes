iframe 内联框架，用来向一个网页中引入另一个网页  
可以用来隔离不同来源的内容，防止恶意代码影响主页面。  
属性，src用来指定要引入的网页的路径  
```html
<iframe src="https://www.4399.com" width="900" height="900"></iframe>
```
```html
    <iframe src="https://www.4399.com" width="900px" height="900px" scrolling="yes"></iframe>
    <iframe src="ext.html" width="1200px" height="1200px" scrolling="yes" name="百度"></iframe>
    <iframe src="ext.html" width="1200px" height="1200px" scrolling="yes" name="B站"></iframe>


    ext.html
    <a href="http://www.baidu.com" target="百度">百度链接</a> <br>
    <a href="http://www.bilibili.com" target="B站">B站链接</a>
```
