''' query server for:
- Total CPU usage
- Total memory usage (Free vs Used including percentage)
- Total disk usage (Free vs Used including percentage)
- Top 5 processes by CPU usage
- Top 5 processes by memory usage
'''
import psutil as p


def print_usage():
    usage = p.cpu_percent(interval=1)

def print_mem_usage():
    memory = p.virtual_memory()

def print_disk_space():
    space = p.disk_usage('/')
    

def print_top5_proccess_usage():
    psutil.process_iter(['fields']):

def print_top5_process_mem():
    psutil.process_iter(['fields']):


        
