tomcat下载安装配置教程
我是使用tomcat下载安装及配置教程_tomcat安装-CSDN博客 此贴来进行安装配置，原文21年已经有些许不同。

下载tomcat
官网：http://tomcat.apache.org/

我们老师让安装8.5以上，所以我直接选择版本9



点击9页面之后看自己所需安装相应的版本，大部分都是Windows 64-bit安装Core版即可
 

配置系统变量
接下来基本一致

1、在电脑点击鼠标右键->点击属性

2、点击高级系统设置->环境变量->新建系统变量

1)、新建系统变量，变量名为CATALINA_HOME

2）、找到系统变量Path，双击空白处或新建即可在末尾加上%CATALINA_HOME%\bin

甚至GBK问题都一致（我记得之前我把cmd编码改成UTF-8了啊）

接下来遇到了独特的错误:

运行startup.bat出现错误代码:

Neither the JAVA_HOME nor the JRE_HOME environment variable is defined

这是我Java问题,直接查看JAVA路径,一看,没配;再一看,java被我假期时候删了(老师说的就是我),重新安装JDK后配置新建系统变量
 

JAVA_HOME=‘JAVA安装路径’(不到bin目录内)

 

然后再在PATH中加入%JAVA_HOME%\bin定位到bin目录在这里插入图片描述

再次尝试startup.bat，搞定。

 

（实验报告写的真是累,水了一篇）