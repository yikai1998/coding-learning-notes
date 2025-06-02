盒子模型 box model  
- 网页的布局 指将元素摆放到网页的不同位置
- 在网页中的每个元素都是一个矩形
- 布局得先设置大小
- 盒子的组成部分：
  - 内容区 content  
    在元素的最内部，用来容纳子元素
  - 边框 border
    盒子的边界，border-width, border-color, border-style  
    border可以简写，同时设置三个样式 `border: solid red 10px`
  - 内边距 padding  
    内容和边框之间的距离
  - box-sizing 用来指定盒子可见框
    ```
    box-sizing: border-box;
    width: 300px;
    height: 300px;
    padding: 20px;
    background-color: #bfa;
    border: 10px red solid;
    margin-top: 100px;
    margin-bottom: 100px;
    padding-top: 100px;
    margin: auto; /*水平垂直居中*/
    当子元素的大小超过了父元素的内容区时，子元素会overflow，如何处理呢？用overflow样式
      可选值：默认visible，hidden隐藏，scroll生成水平和垂直的滚动条，auto根据需要自动判定生成滚动条
    
    ```
```html
<!--小练习-->
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document-2025-05-15</title>
    <style>
        .w1 {
            border: 2px black solid;
            color: red;
            height: 50px;
            background-color: pink;
            width: 400px;
            margin: auto;
            /*
            margin: auto; 对 <p> 元素不起作用的原因是 <p> 元素默认是块级元素（block-level element），但它的宽度是自动的（默认情况下宽度会根据内容自动调整），
            而 margin: auto; 通常用于水平居中块级元素时，需要元素的宽度是固定的（或者设置了宽度）。
            解决方法: 为了让 margin: auto; 起作用，你需要给 .w1 设置一个固定的宽度
            */
            text-align: center;  /*水平居中用text-align*/
            line-height: 50px;  /*将行高设置成和元素高度一样*/
        }
    </style>
</head>
<body>

    <p class="w1">
        今天去游泳，很开心。
    </p>

</body>
</html>
```
    
# 来源：《新手学html+css》-- 北京希望电子出版社  
```txt
background-image: url(括号里填图片链接/地址); 必须同时设置高度和宽度
background-repeat: no-repeat; 绑定的图片只出现一次
background-repeat: repeat; 绑定的图片会重复出现，横向和纵向都会重复
background-repeat: repeat-x; 绑定的图片会重复出现，横向
background-repeat: repeat-y; 绑定的图片会重复出现，纵向
```
```html
<style>
    .temp-div-1 {
    color: white;
    background-image: url(kakashi.jfif);
    width: 400px;
    height: 800px;
    background-repeat: repeat-x;
    }
</style>
<body>
    <div class="temp-div-1" c>
        测试背景图片
    </div>
</body>
```
