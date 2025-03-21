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
- 法5 title*="cba" 表示包含abc的title
- 法6+ 多个选择器一起写，则为同时满足
```html
div[title=hello] {
  color: purple
}
p.class_name {
  ...
}

A  B
Selects all B inside of A

`p, .fun` selects all p elements as well as all elements with class="fun"

`p *` selects any element inside all p elements.
```

---

### 分组选择器  
同时选中多个选择器对应的元素  
语法：选择器1，选择器2，选择器3，...，选择器n {}  
```
#p1, .p2, div {
  color: red;
}
等价于
#p1 {
  color: red;
}
.p2 {
  color: red;
}
div {
  color: red;
}
```

<hr>

### 关系选择器  
选中指定元素的子元素（不含孙元素）
```
父选择器 > 子选择器 {
  color: red;
}
``` 
选中指定元素的后代元素
```
父选择器 后代选择器 {
  color: red;
}
```
选择紧随其后的一个兄弟元素（必须同时满足“紧随其后”和“弟”，只要满足 都执行）
```
兄 + 弟 {
  color: red;
}
```
选择后边的所有兄弟元素
```
兄 ~ 弟 {
  color: red;
}
```

---

### 伪类选择器 pseudo  
伪类是一个特殊的类，用来表示元素的特殊状态  
- 比如超链接，一个链接有没有被访问过，就是一种特殊状态；在css中，可以使用
- \<a> `:visited`表示访问过的超链接，`:link`未访问过的超链接，
- visited只能改变文字颜色
- `:hover`表示当鼠标移入
- `:active`表示当鼠标点击时
- `:empty`表示空元素，比如<div>...</div>之间没任何东西
- `li:first-child`表示 为第一个子元素的li标签（无所谓父元素是谁，但div必须是第一个儿子）等同于`li:nth-child(1)`
- `li:first-of-type`表示 为第一个li标签（无所谓被包在哪个类型里，反正是第一个li）等同于`:nth-of-type(n)`
- `li:nth-last-child(n)` `li:nth-last-of-type(n)` 相似原理
- `p:not(.p1)` 表示针对除了class为p1的p标签； 同理 `p:not(:nth-child(3))`
```
<style>
  p:hover {
    color: yellow;
  }
  a:visited {
    color: red;
  }
</style>
```

伪元素表示特殊的位置，用`::`开头  
- `::before`表示元素的开始位置，开始标签之后
- `::after`表示元素的结束位置，结束标签之前
- content里的内容是通过css添加的，不算是网页中的正是内容，所以爬虫抓不到数据
- 可以统一批量的给标签文字前加内容，比如符号
```
<style>
  div::before {
    content: "插入内容xxxx";
    color: red;
  }
</style>
```
- `::selection`
- `::first-line`
- `::first-letter`

---

### 样式的继承
```
<head>
    ...
    <style>
        div {
        color: green;
        }
    </style>
</head>
<body>
    <div>
        我是div
        <p>我是div中的p元素</p>
    </div>
</body>
```
设置给祖先元素的样式（背景、边框、布局相关的样式除外），同时也会反映到其后代元素上  

---

### 优先级  
内联样式 > id选择器 > 类和伪类 > 元素选择器 > 通配  
注意：  
```
div.box1 [0, 0, 1, 1]
.box1 [0, 0, 1, 0]
所以现在变成 div.box1优先级更高了
```
如果优先级一样，则靠下的更优先  
如果为样式添加 !important，则该样式获得最高优先级  
```
* {
  color: grey !important
}
```
