# 2018-12-23
## 第九页
Docker需要用到Linux的cgroups、namespace等特性所以目前只能运行在Linux环境下，当然通过虚拟机，也可以在Windows和MAC上使用docker.  
Docker是一个CS架构的，它的Docker Daemon作为Server端，在宿主机上以后台守护进程的心事运行，Docker Client的使用比较的灵活。既可以在笔记说那个以bin命令形式
（如docker info、docker start）发送命令，也可以在远端通过RESTful API的形式发送指令; Docker的Server端接收指令并把指令分解为一系列的任务去执行。  
