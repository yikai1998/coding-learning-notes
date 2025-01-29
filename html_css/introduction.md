前端就是写网页的  
c/s架构：customer客户端 service服务端  
- 用户通过客户端来使用软件
- 服务器为客户提供各种服务器
客户端的呈现形式：
- 传统图形化界面，如 qq，都需要先安装，且跨平台性差(ios, windows, mac, ...)从而导致开发成本较高 
- 以网页为界面(interface)，如 淘宝京东知乎，不需要安装，靠浏览器运行所以跨平台性好 开发成本低。 b/s架构， browser

---

根据w3c(万维网中的一切标准)的规范，一个网页会被分成三个部份：  
1. html负责网页的结构，类似骨架，哪儿是标题，哪儿是图片，...
2. css负责网页的表现，比如网页的颜色，布局，好不好看
3. javascript负责网页和用户的交互行为

w3c的标准可以直接去[https://developer.mozilla.org/en-US/docs/Learn_web_development](https://developer.mozilla.org/en-US/docs/Learn_web_development)查

---

HTML - Hyper Text Markup Language  
网页的扩展名是html, 网页最终由浏览器渲染呈现  
在网页中使用html标签作标记 告诉浏览器网页中的不同内容 学习html就是学习各种标签  
html标签写法：  
成对出现 如 \<tag>\</tag>  

---

网页的基本结构  
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

</body>
</html>
```
- \<!DOCTYPE html>  
文档声明，用来声明当前网页的版本，表示当前网页是遵循html5规范的
- \<html lang="en">  
html根标签，一个网页有且仅有一个根标签，其他标签都得在它的内部。lang属性用来设定当前网页语言
- \<head>
html的子标签(子元素)，表示网页的头部，可以用来设置网页的各种信息，head中的内容不会在网页中直接显示
  - title是head的子元素，title的内容在网页标签上显示
  - meta是head的子元素，用来设置网页的元数据， charset是属性 utf-8是属性值，主要用来避免乱码问题
- \<body>
网页中所有可见的内容都应该写在body里面

小技巧：输入“感叹号”+Tab键，会自动帮你补全生成一个基本结构  
