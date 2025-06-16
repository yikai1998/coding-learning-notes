```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        table {
            width: 80%;  /* 表示元素的宽度是其父元素宽度的80% */
            border-collapse: collapse;  /* 把相邻的线都合并 */
        }
        td {
            border: 1px solid blue;  /* 会导致双线，因为每个td是独立的 */
        }
    </style>
</head>
<body>
    <table>
        <!-- 表格标题-->
        <caption>西游记</caption>
        <!-- 表格头部-->
        <thead>
        <tr>
            <td>学号</td>
            <td>姓名</td>
            <td>性别</td>
            <td>年龄</td>
            <td>住址</td>
        </tr>
        </thead>

        <!-- 表格主体-->
        <tbody>
        <tr>
            <td>1</td>
            <td>孙悟空</td>
            <td>男</td>
            <td>18</td>
            <td>花果山</td>
        </tr>
        <tr>
            <td>2</td>
            <td>猪八戒</td>
            <td>男</td>
            <td>17</td>
            <td>高老庄</td>
        </tr>
        <tr>
            <td>3</td>
            <td>沙和尚</td>
            <td>男</td>
            <td>19</td>
            <td>流沙河</td>
        </tr>
        </tbody>

        <!-- 表格底部-->
        <tfoot>
        <tr>
            <!-- 一个单元格要占3个格子的位置；rowspan同理-->
            <td colspan="3"></td>
            <td>合计: </td>
            <td>3人</td>
        </tr>
        </tfoot>
    </table>
</body>
</html>
```
