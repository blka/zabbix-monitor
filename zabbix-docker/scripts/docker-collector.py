#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docker import Client
import json
import sys
class Job(object):
    def __init__(self):
        self._monitor = None

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self,args):
#        print args
	ConName = args[0]
        ConItem = args[1]
        cli = Client(base_url='unix://var/run/docker.sock', version='1.19')
        stats_obj = cli.stats(ConName)
        old_result = json.loads(stats_obj.next())
        new_result = json.loads(stats_obj.next())
        stats_obj.close()

        if ConItem == 'cpu_total_usage':
            self._monitor = new_result['cpu_stats']['cpu_usage']['total_usage'] - old_result['cpu_stats']['cpu_usage']['total_usage']
        elif ConItem == 'cpu_system_uasge':
            self._monitor = new_result['cpu_stats']['system_cpu_usage'] - old_result['cpu_stats']['system_cpu_usage']
        elif ConItem == 'cpu_percent':
            cpu_total_usage = new_result['cpu_stats']['cpu_usage']['total_usage'] - old_result['cpu_stats']['cpu_usage']['total_usage']
            cpu_system_uasge = new_result['cpu_stats']['system_cpu_usage'] - old_result['cpu_stats']['system_cpu_usage']
            cpu_num = len(old_result['cpu_stats']['cpu_usage']['percpu_usage'])
            self._monitor = round((float(cpu_total_usage)/float(cpu_system_uasge))*cpu_num*100.0,2)
        elif ConItem == 'mem_usage':
            self._monitor = new_result['memory_stats']['usage']
        elif ConItem == 'mem_limit':
            self._monitor = new_result['memory_stats']['limit']
        elif ConItem == 'mem_percent':
            mem_usage = new_result['memory_stats']['usage']
            mem_limit = new_result['memory_stats']['limit']
            self._monitor = round(float(mem_usage)/float(mem_limit)*100.0,2)
        elif ConItem == 'network_rx_bytes':
            self._monitor = new_result['network']['rx_bytes'] - old_result['network']['rx_bytes']
        elif ConItem == 'network_tx_bytes':
            self._monitor = new_result['network']['tx_bytes'] - old_result['network']['tx_bytes']

    @monitor.deleter
    def monitor(self):
        del self._monitor

if __name__ == "__main__":
    
    tup = ()
    
    job =Job()
    job.monitor = sys.argv[1],sys.argv[2]
    print job.monitor
    del job.monitor

    


