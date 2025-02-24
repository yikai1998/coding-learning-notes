## css选择器  
通过css选择器，可以选中页面中的指定元素，从而为这些元素设置样式  

---

### 基本选择器  
- 元素选择器（根据标签名选择多个元素）
```css
div {
  color: red;
}
```
- id选择器（根据元素的id属性选中一个元素）
```css
#id_name {
  color: red;
}
```
- 类选择器（根据元素的class属性选择多个元素）  
class和id类似，每一个元素都可以指定，用来为元素进行分类，可以重复，甚至可以为一个元素赋予多个class  
```css
.class_name {
  color: red;
}
```
```css
    <style>
        .ib {
            color: grey;
        }
    </style>
...
<p id="secondp2" class="sb ib">楚河当日的那个</p>
<!--多个class，中间用空格隔开，开头不能是数字-->
```
- 通配选择器（选择页面中的所有元素）
```css
* {
  color: red;
}
```

---

### 属性选择器  
根据元素的属性来选中元素  
- 法1 只要有title属性，全都纳入 (title里写的东西，会使鼠标停在页面对应内容上时出现对应内容  )
```html
<head>
    <meta charset="UTF-8">
    <title>测试标签</title>
    <style>
        [title] {
            color: pink;
        }
    </style>
</head>
<body>
<p id="firstp1" class="sb" title="abc">锄禾日啖顾问</p>
<p id="secondp2" class="sb ib">楚河当日的那个</p>
<p id="third3" class="sb ib" title="cba">汗滴禾下土认识</p>
</body>
```
- 法2 选中特定title的内容
```html
<head>
    <meta charset="UTF-8">
    <title>测试标签</title>
    <style>
        [title="cba"] {
            color: pink;
        }
    </style>
</head>
<body>
<p id="firstp1" class="sb" title="abc">锄禾日啖顾问</p>
<p id="secondp2" class="sb ib">楚河当日的那个</p>
<p id="third3" class="sb ib" title="cba">汗滴禾下土认识</p>
</body>
```
- 法3 title^="cba" 表示以abc开头的title
- 法4 title$="cba" 表示以abc结尾的title
