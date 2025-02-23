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
