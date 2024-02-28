# tomcat之网页开发基础复习

<!DOCTYPE>**声明** :HTML标准规范
</!doctype>


`<html>` : 根标签

`<head>`: 头部标签  内含`<title><meta><link><style>`

`<body>`: 主体

`<body></body>`

## html标签

单标签: `<标签名 \>`

双标签:`<标签名>内容<标签名>`

注释标签:`<!--注释-->`

```html
<p></p>,<br/>,<span></span>,

```

表格标签:

```html
<tr>
    <td>2333</td>
</tr>
```

### 表单标签:

表单域`<form>`

```html
<form action ="URL 地址" method = "提交方式" name = "表单名称">
    各种表单控件
</form>
```

action -- 表单提交地址

method --**GET** or **POST** (默认GET保密性差,且有数量限制,POST保密性高,且可提交大量数据,开发中常用POST)

### 表单控件

`<input/>`

```html
<input type = "控件类型" />
```

input type --**text** 文本输入,**password** 密码输入,**radio** 单选 ,**checkbox** 复选,**file** 文件上传,**submit** 提交 ,**reset** 重置

```html
<textarea cols = "每行字符数" rows = "显示的行数">
	文本内容
</textarea>
```

### 列表标签

```html
<ul>
    <li>无序</li>
    <li>阿巴阿巴</li>
</ul>

<ol>
    <li>有序1</li>
    <li>有序2</li>
</ol>

<dl>
<dt>名词1</dt>
    <dd>名词1描述</dd>
<dt>名词2</dt>
    <dd>名词2描述</dd>
    <dd>名词2描述</dd>
</dl>

```

### 超链接标签

```html
<a href = "跳转目标" target = "目标窗口弹出方式">文本or图像</a>
```

`target` **_self** 默认值,原窗口打开;**_blank** 新窗口打开;**_parent** 父框架集打开;**_top** 整个窗口中打开

### 图像标签

```html
<img src = "图像URL"/>
```

可加width ,height ,border....

# CSS

```css
选择器{
	属性1:属性值1;
	属性2:属性值2;
}
```

长度--像素(px),百分比(%)

颜色-- red,green,blue....#FF0000,#FF6600,#29D794......rgb(255,0,0).......

### 行内式

结构不与样式分离,不建议使用

```html
<标签名 style = "属性1:属性值1;.....">内容</标签名>
```

### 内嵌式 

head 提前加载

```html
<head>
   	<style type = "text/css" >
        选择器{属性1:属性值1;......}
    </style>
</head>
```

### 外链式

```html
<head>
	<link href = "CSS文件路径" type = "text/css" rel = "stylesheet" />
</head>
```

**rel** : 表示 定义当前文档与被链接文档之间的关系 ,指定为stylesheet, 样式表文件

css文件:

```css
<style type = "text/css">
h2{
    text-align :center;
}
div{
    border:1px solid #CCC; width : 300px; height : 80px;color:purple;
    text-align:center;
}
</style>
```

HTML文档:

```html
<head>
   	<link href = "style.css" type = "text/css" rel = "stylesheet" />
</head>
<body>
    <h2>
        外链式css样式
    </h2>
    <div>
        链入式
    </div>
</body>
```

### 导入式

```html
<style  type = "text/css"> 
    @import url (CSS 文件路径);<!--或 @import "CSS文件路径";-->
</style>
```

HTML文档更改:

```html
<head>
   	 <style  type = "text/css"> 
    @import url (CSS 文件路径);<!--或 @import "CSS文件路径";-->
	</style>
</head>
<body>
    <h2>
        外链式css样式
    </h2>
    <div>
        链入式
    </div>
</body>
```

## CSS 选择器&常用属性

**标签选择器** 

```css
标签名{属性1:属性值1;......}
```

**类选择器**

```css
.类名{属性1:属性值1;.....}
```

**id选择器** 

```css
#id名{属性1:属性值1;.....}
```

**通配符选择器**

```
*{属性1:属性值1;.....}
```

## Java Script

### JavaScript的引入方式

#### 行内式

```html
<body>
    <input type="button" value = "点我" onclick="alert('行内式') " / >
</body>
```

#### 内嵌式

```html
<head>
    <script type = "text/javascript" >
	//javascript代码在此处
</script>
</head>
```

#### 外链式

```html
<head>
    <title>js外链式</title>
    <script type="text/javascript" src="jsDemo.js"></script>
</head>
```

#### 数据类型

- **Number** 数值部分不分整型&浮点型 ,
- **String** 字符串' '," "
- **Boolean**  true or false
- **Object**  对象类型  一组数据&功能的键值对集合
- **Null**  
- **Undefined**  未定义   变量被创建,但未赋值

## DOM 相关知识

可以一种独立`平台&语言`的方式  来`访问&修改`一个文档的`内容&结构`

- parentNode
- childNode
- firstChild
- lastChild

### 获取文档中指定的元素

1) id

```
document.getElementById("userId");
```

2. name

```
document.getElementsByName("userName") [0];
```

## BOM 相关知识

BOM提供了独立于内容且可与浏览器窗口进行交互的对象,

BOM包含DOM