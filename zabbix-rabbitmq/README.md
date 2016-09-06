Zabbix RabbitMQ Monitoring Plugin

A Zabbix plugin to monitor RabbitMQ. This plugin is very basic and needs lots more work for production usage.

This plugin requires the RabbitMQ HTTP Management to be installed.


Installation Instructions
```
1、将config.php zabbix_rabbitmq_plugin.php zabbix_rabbitmq_plugin.sh 复制到zabbix脚本运行目录
2、将config.php的配置项改成你需要的。
	ZABBIX_SERVER为zabbix服务端的IP地址
	ZABBIX_HOSTNAME为你当前zabbix被监控端的主机名。因为该监控方式采用zabbix trapper方式，所以必须为主机名，且与服务端上配置的该主机的主机名一致，默认通过php自动获取，无需修改。
	API_HOSTNAME为rabbitmq的地址，默认为本机
	API_PORT为rabbitmq的管理端口，默认为15672
	API_USER为rabbitmq的认证用户，默认使用guest用户
	API_PASS为认证用户的密码
3、因为监控脚本为php脚本，需要预装php环境，并将php命令链接至标准PATH目录中
4、可直接运行zabbix_rabbitmq_plugin.sh脚本进行测试，会在/tmp目录下生成两个文件，分别为zabbix_rabbitmq_plugin.data和zabbix_rabbitmq_plugin.log。data为上报给zabbix server的内容，log为日志文件，确认log文件没有报错。
5、配置crontab，实现每分钟自动上报：
	* * * * * /etc/zabbix/scripts/zabbix_rabbitmq_plugin.sh
```
