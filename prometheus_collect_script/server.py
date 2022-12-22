from prometheus_client import Gauge
from collector import Collector


import psutil,socket



host = socket.gethostname()

ram_metric = Gauge("memory_usage_bytes", "Memory usage in bytes.",
                       {'host': host})

cpu_metric= Gauge("cpu_usage_percent", "CPU usage percent.",
                       {'host': host})

disk_metric = Gauge('disk_usage_percent','Disk usage percent',{'host':host})





def main(*args, **kwargs):
    while True:
        kwargs['col'].gather_data(CPU_USAGE=cpu_metric,MEM_USAGE=ram_metric,DISK_USAGE=disk_metric)

if __name__ == '__main__':
    collect = Collector(8021,2)
    
    collect.start_server()

    
    main(col=collect)

    
        
