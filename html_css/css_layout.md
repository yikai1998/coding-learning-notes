- 原始的布局方式 table
- 网格布局 grid
  - 和table类似
  - 将网页分成一列列一行行，以帮助完成布局
  - 结构简单，样式复杂
- 弹性盒 flex
  - 适用于单行单列
  - 多行多列时要使用不同的结构组合使用
  - 结构复杂，样式简单

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
        body {
            display: grid;
            grid-template-columns: repeat(4, 1fr);  /* 每列多少间距 */
            grid-template-rows: 150px 200px 200px 150px;  /* 每行多少间距 */
            margin: 0 150px;
        }
        .box1 {
            background-color: red;
            grid-column-start: 1;
            grid-column-end: -1;  /* 独占一行 */
        }
        .box2 {
            background-color: yellow;
            grid-row-start: 2;
            grid-row-end: -2;
        }
        .box3 {
            background-color: green;
            grid-column-start: 2;
            grid-column-end: -1;
        }
        .box4 {
            background-color: blue;
        }
        .box5 {
            background-color: grey;
        }
        .box6 {
            background-color: purple;
        }
        .box7 {
            background-color: orange;
            grid-column-start: 1;
            grid-column-end: -1;
        }


    </style>
</head>
<body>
    <div class="box1">网页头部</div>
    <div class="box2">菜单</div>
    <div class="box3">上半部分</div>
    <div class="box4">图片</div>
    <div class="box5">图片</div>
    <div class="box6">图片</div>
    <div class="box7">底部</div>
</body>
</html>
```
