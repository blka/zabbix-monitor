

1、目录说明：
`confiure`目录下为zabbix agent监控docker的配置文件。
`templates`目录下为zabbix监控docker的模版。
`scripts`目录下为用于自动发现docker容器及收集数据的脚本。

2、要运行scripts目录下的脚本，需要zabbix agent端的zabbix用户有sudo权限，配置如下：
编辑 /etc/sudoers，注释掉如下行：
Defaults    requiretty
添加如下行：
Cmnd_Alias SUPER = /usr/bin/*, /etc/zabbix/scripts/*
zabbix  ALL=(ALL)       NOPASSWD:SUPER

3、需要安装python-docker-py包：
yum install -y python-docker-py

