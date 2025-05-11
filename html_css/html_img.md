 使用img标签向页面中引入图片，他是一个自结束标签  
- src属性表示要引入的图片的路径
- alt属性是对图片的描述；一般不会显示，如果加载失败了 如路径不存在 则会显示文字描述；帮助搜索引擎识别图片
- width height 属性 规定图片大小，建议只改一个 确保比例不变
- 如：\<img src="xxx.gif"/"urladdress">
  - 绝对路径
  - 相对路径 ./表示当前目录 可以省略；../表示当前目录的上一级目录

---

常见的图片格式  
jpg 用来显示图片，颜色丰富但不透明，支持压缩  
gif 颜色单一的图片 支持简单的透明，或动图   
png 颜色丰富的图片，支持透明效果  
webp 是谷歌专门为浏览器推出的一种格式，兼具上述优点，但部分浏览器还不支持这种格式  
base64 是一种编码格式，可以把图片转换成字符，然后直接进行编码，编码后可以直接在网页引入图片，放在src，他是和网页一起加载 所以会比一般的src外部路径引入图片要加载得更快，但不要多用，因为会影响网页本身的加载速度  

---

```
<a href="kakashi.jfif"><img src="kyubi.jfif "></a>
```
展示的时候是kyubi，点击后下载的是kakashi；href也可以是网上的图片链接

---

### 拓展
- 引入视频  
```
<video width="640" height="360" controls>
    <source src=https://th.bing.com/th?&id=OMB.ApKJhjpolHenRQ_1744337786&w=null&h=null&c=7&pid=1.7&rs=1" type="video/mp4">
    Your browser does not support the video tag. Please use a modern browser to view this video.
</video>
```
