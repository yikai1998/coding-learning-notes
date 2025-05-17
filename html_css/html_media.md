# 来源：《新手学html+css》-- 北京希望电子出版社

## 多媒体

#### 滚动字幕  
marquee
behavior是移动方式，默认scroll循环滚动，slide滚动单次后停止，alternate来回滚动  
bgcolor width height  
direction 滚动方向 left right up down  
scrollamount 滚动速度  
loop 滚动次数  
vspace hspace 字母上下左右空白区域，无须px  
scrolldelay 停顿时间  
onMouseOver 定义鼠标划进时的效果 this.stop()  
onMouseOut 定义鼠标划出时的效果 this.start()  
可以是文字字幕，也可以是图片  
```html
<marquee behavior="alternate" direction="up" scrollamount="5" height="80" bgcolor="red" onMouseOver="this.stop()" onMouseOut="this.start()">这是一条滚动的字幕</marquee>
```
