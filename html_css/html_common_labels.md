title表示标题标签，文字会显示到标签页。而且搜索引擎在搜索页面时，会通过title的内容来识别网页的主要内容。  

h1 h2 h3 h4 h5 h6 标题标签。通常一个页面只有一个h1，搜索引擎也会识别h1，在seo中h1的重要性仅次于title。  

blockquote缩进，是一整段的缩进

p 段落标签。  

b粗体，i斜体，u下划线，del/s/strike删除线

br 换行标签。\<br>  

hr 水平线标签。\<hr>  

在网页中展示特殊符号，用 &实体名; 比如 \&lt; 小于号；\&nbsp; 空格号；\&copy; 版权符号；  

html中会忽略多个空格和换行，至多被识别一次。如果希望有若干个空格，可以用\&nbsp;。如果希望有若干个换行，那就用\<br>。  

列表  
- 有序列表  
  使用ol来创建有序列表，在ol中使用li来表示列表项目
  ol type, 默认1数字标号，A大写字母，同理I, i, a
  ```html
  <ol>
      <li>大老婆</li>
      <li>小老婆</li>
  </ol>
  ```
- 无序列表
  使用ul来创建有序列表，在ul中使用li来表示列表项目
  ul type， 默认disc实心圆，circle空心圆，square实心小方块
  ```html
  <ul>
      <li>大老婆</li>
      <li>小老婆</li>
  </ul>
  ```
  ```html
  <ul type="square">
      <li>钱是老板的</li>
      <li>命是自己的</li>
  </ul>
  ```
  
  列表间可以相互嵌套
  ```html
    <ul>
        <li>
            大老婆
            <ol>
                <li>大乔</li>
                <li>小乔</li>
            </ol>
        </li>
        <li>
            小老婆
            <ol>
                <li>貂蝉</li>
                <li>秋香</li>
            </ol>
        </li>
    </ul>
  ```
- 定义列表
  使用dl来创建一个定义列表，dt来定义被描述的内容，dd来描述内容
  ```html
    <dl>
        <dt>
            男人
            <dd>有小鸡鸡</dd>
        </dt>
        <dt>
            女人
            <dd>没有小鸡鸡</dd>
            <dd>有波波</dd>
        </dt>
    </dl>
  ```

---

pre 预格式，保留你输入的文本的自身格式  

code 代码格式

---
# ai整理的回答  
\<table>：表格标签，用于创建表格。  
一行行写的，先table，再tr，再th/td  
表格table标签里可以没有表头单元格th，但是不能没有单元格数据标签td  
```html
<table border="1">
  <tr>
    <th>表头1</th>
    <th>表头2</th>
  </tr>
  <tr>
    <td>单元格1</td>
    <td>单元格2</td>
  </tr>
</table>
```
```html
<table cellspacing="50px" cellpadding="2px" border="10px" bordercolor="blue" align="center">
    <caption>暑假作业</caption>
    <tr>
        <th>唐诗三百首</th>
        <th>宋词一百篇</th>
    </tr>
    <tr>
        <td>飞流直下三千尺，疑是银河落九天。</td>
        <td>蓦然回首，那人却在，灯火阑珊处。</td>
    </tr>
    <tr>
        <td>垂死病中惊坐起，暗风吹雨入寒窗。</td>
        <td>王师北定中原日，家祭勿忘告乃翁。</td>
    </tr>
    <tr>
        <td align="center" colspan="2">编辑中</td>
    </tr>
</table>
```

\<form>：表单标签，用于创建表单。
```html
<form>
  <label for="username">用户名：</label>
  <input type="text" id="username" name="username"><br>
  <label for="password">密码：</label>
  <input type="password" id="password" name="password"><br>
  <input type="submit" value="提交">
</form>
```

\<span>：行内容器，用于分组HTML元素。这个标签本身是没有任何意义的，只有结合css才可以看出效果  
```html
<p>这是一个<span style="color:red;">红色</span>的文本。</p>
```
