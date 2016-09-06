<?php
// Zabbix Configuration
define('ZABBIX_SERVER', '127.0.0.1');
define('ZABBIX_HOSTNAME', exec('hostname'));

// RabbitMQ Configuration
define('API_HOSTNAME', '127.0.0.1');
define('API_PORT', 15672);
define('API_USER', 'guest');
define('API_PASS', 'guest');
