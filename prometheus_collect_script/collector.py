from prometheus_client import Gauge, Histogram,Info, start_http_server


import psutil,time

global_path = ['/','/boot/efi']

class   Collector:
    disk_usage = []

    def __init__(self,port,update_period) -> None:
        self.port = port
        self.update_period = update_period
        

    
    def __Gauge_CPU_Collector(self,CPU_USAGE):
        for c,p in enumerate(psutil.cpu_percent(interval=1,percpu=True)):
            CPU_USAGE.labels(f'CPU Capacity |  Core: {c}').set(p)
        # SYS_USAGE.labels('Memory Capacity').set(psutil.virtual_memory().percent)
        # for subelem in self.disk_usage:
        #     if subelem in global_path:
        #         SYS_USAGE.labels(f'PATH={subelem} ,Disk Capacity % :').set(psutil.disk_usage(subelem)[3])

    def __Gauge_MEM_Collector(self,MEM_USAGE):
        # MEM_USAGE.labels('Memory Used').set(psutil.virtual_memory().used)
        MEM_USAGE.labels('Memory Capacity').set(psutil.virtual_memory().percent)
        
        # MEM_USAGE.labels('Swap Capacity').set(psutil.swap_memory().used)

    def __Gauge_DISK_Collector(self,DISK_USAGE):
        for subelem in self.disk_usage:
            if subelem in global_path:
                DISK_USAGE.labels(f'PATH={subelem}, Disk Capacity % !').set(psutil.disk_usage(subelem)[3])



    def gather_data(self,*args, **kwargs):
        partitions = psutil.disk_partitions(all=False)
        for p in partitions:
            self.disk_usage.append(p.mountpoint)
       

        self.__Gauge_CPU_Collector(kwargs['CPU_USAGE'])
        self.__Gauge_MEM_Collector(kwargs['MEM_USAGE'])
        self.__Gauge_DISK_Collector(kwargs['DISK_USAGE'])

        
        time.sleep(self.update_period)

    def start_server(self):
        start_http_server(self.port)
