import socket
from contextlib import closing
   
def check_socket(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex((host, port)) == 0:
            print("Port is open")
        else:
            print("Port is not open")


check_socket('stage.bks.econostic.net',9090)


from prometheus_api_client import PrometheusConnect, MetricSnapshotDataFrame, Metric

prom = PrometheusConnect()


my_label_config = {'cluster': 'my_cluster_id', 'label_2': 'label_2_value'}
metric_data = prom.get_current_metric_value(
    metric_name='cpu_usage_percent',
    label_config=my_label_config
    )

print(metric_data)


metric_df = MetricSnapshotDataFrame(metric_data)


import psutil
import time


def display_usage(cpu_usage,mem_usage,bars=50):
    cpu_percent = (cpu_usage/100.0)
    cpu_bar = "█" * int(cpu_percent * bars) +  '-' * (bars-int(cpu_percent*bars))
    
    mem_percent = (mem_usage/100.0)
    mem_bar = "█" * int(mem_percent * bars) +  '-' * (bars-int(mem_percent*bars))
    
    
    print(f"\rCPU Usage : |{cpu_bar}| {cpu_usage:.2f}%  ",end='')
    print(f"MEM Usage : |{mem_bar}| {mem_usage:.2f}%  ",end='\r')
    
    
    
while True:
    display_usage(psutil.cpu_percent(),psutil.swap_memory().percent,30)
    time.sleep(0.5)
import subprocess

services = ['apache2']
for service in services:
    try:
        status = subprocess.check_output("/etc/init.d/"+service+" status", shell=True)
    except subprocess.CalledProcessError as e:
        status = "is stopped"

        if ("is stopped" in status):
                print (service + "  - Stopped")
                print( service + "  - Trying to start")
                service_start = subprocess.check_output("/etc/init.d/"+service+" start", shell=True)
        else:
                print (service + "  - Running ")