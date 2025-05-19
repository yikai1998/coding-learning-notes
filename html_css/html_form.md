# 来源：《新手学html+css》-- 北京希望电子出版社

## 表单 包括 输入框、单选框、复选框 等  

action 指定表单提交的目标URL 里面填写的链接地址和超链接地址的写法用法是一样的  
method 表单提交时的跳转方法 get(数据会附加在URL中，适合简单的查询)或post(数据会包含在请求体中，适合提交敏感信息或大量数据)  
enctype 指定表单数据的编码类型  
name 为表单指定一个名称，方便在JavaScript中引用  
id 为表单指定一个唯一的标识符，方便在CSS和JavaScript中引用  
input 输入框  
- required 表示这个输入框是必填的
- id 唯一标识符
- name 表单提交时，这个输入框的数据会以 name 为键发送到服务器
- type = text 输入文字  
- type = mail 输入邮箱，会自动校验邮箱格式
- type = password 只会看到代替出现的密码保护符号，到底是*还是圆点 取决于浏览器
- type = radio 单选框 value和name都是用来以后和js绑定的 如果希望实现单选效果，必须value和name都填，且都为同一个值 checked="checked"代表默认选择
```html
    <input type="radio" value="choice" name="choice" checked="checked"> choiceA
    <input type="radio" value="choice" name="choice"> choiceB
```
- type = checkbox 多选框 value和name都是用来以后和js绑定的 checked="checked"代表默认选择
```html
    <input type="checkbox" value="choice1" name="choice1" checked="checked"> choiceA
    <input type="checkbox" value="choice2" name="choice2" checked="checked"> choiceB
    <input type="checkbox" value="choice3" name="choice3"> choiceC
```
