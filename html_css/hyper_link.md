使用\<a>标签来定义一个超链接  
href属性用来指定跳转到的位置  
target 用来指定页面打开的位置，_blank表述新页面打开；_parent表示父窗口 和iframe配合 点击以后会让外层页面跳转；默认是_self 意思是当前页面打开  
```html
<a href="https://www.baidu.com">这是百度首页</a>
```
```html
<a href="模拟数据.xlsx">这是一个内部文件路径，点击以后会下载</a>
```
```html
<a href="#">回到页面顶部</a>
```

元素的id属性  
在网页中可以为元素设置一个id属性，他是唯一标识，不能重复 否则会报错  
一般都用小写  
#id 表示跳转到页面的指定位置  
```html
<p id="p1">hello</p>
...
<a href="#p1">跳转到id为p1的元素</a>
```
