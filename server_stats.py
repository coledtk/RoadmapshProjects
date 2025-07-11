''' query server for:
- Total CPU usage
- Total memory usage (Free vs Used including percentage)
- Total disk usage (Free vs Used including percentage)
- Top 5 processes by CPU usage
- Top 5 processes by memory usage
'''
import psutil 


def print_usage():
    usage = psutil.cpu_percent(interval=1)
    return usage
def print_mem_usage():
    memory = psutil.virtual_memory()
    mfree = memory[4]
    mused = memory[3]
    mpercentage = memory[2]
    return mfree, mused, mpercentage
def print_disk_space():
    space = psutil.disk_usage('/')
    dfree = space[2]
    dused = space[1]
    dpercentage = space[3]
    return dfree, dused, dpercentage

def print_top5_proccess_usage():
    proc5 = psutil.process_iter(['pid', 'name', 'usage']):
    
def print_top5_process_mem():
    psutil.process_iter(['fields']):
''' query server for:
- Total CPU usage
- Total memory usage (Free vs Used including percentage)
- Total disk usage (Free vs Used including percentage)
- Top 5 processes by CPU usage
- Top 5 processes by memory usage
'''
import psutil 


def print_usage():
    usage = psutil.cpu_percent(interval=1)
    return usage
def print_mem_usage():
    memory = psutil.virtual_memory()
    mfree = memory[4]
    mused = memory[3]
    mpercentage = memory[2]
    return mfree, mused, mpercentage
def print_disk_space():
    space = psutil.disk_usage('/')
    dfree = space[2]
    dused = space[1]
    dpercentage = space[3]
    return dfree, dused, dpercentage

def print_top5_proccess_usage():
    proc5 = psutil.process_iter(['pid', 'name', 'usage']):
    
def print_top5_process_mem():
    psutil.process_iter(['fields']):
