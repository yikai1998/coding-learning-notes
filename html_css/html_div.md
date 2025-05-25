div是一个空标签  
div和css配合才能设计布局，可以减少很多标签属性  
```html
    <div style="color:red;">
        这句话是红色的
    </div>  
```
嵌套div  
```html
    <div style="border:1px solid blue; width:200px; height:150px;">
        <div style="border:1px solid red; width:100px; height:100px;">
            今天天气不错（嵌套）
        </div>
        心情也不错（最外层）
    </div>
```
- 浮动样式
```html
    <div style="float:right;">
        <div style="border:1px solid red; width:100px; height:100px;">
            今天天气不错（嵌套）
        </div>
        心情也不错（最外层）
    </div>
```
- 左右框架
```html
    <div style="border:1px solid blue; height:150px;">
        <div style="float:right;">
            心情也不错（最外层）
        </div>
        <div style="float:left">
            今天天气不错（嵌套）
        </div>
    </div>
```
- 上下框架 clear:both表示清除浮动，会导致标签里的框架被自动换行
```html
    <div style="border:1px solid blue; height:150px;">
        <div style="clear:both;">
            心情也不错（最外层）
        </div>
        <div style="clear:both;">
            今天天气不错（嵌套）
        </div>
        <div style="float:right;">
            我咋不觉得呢
        </div>
    </div>
```
