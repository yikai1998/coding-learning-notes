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
    ...
    ```
    
