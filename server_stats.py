''' query server for:
- Total CPU usage
- Total memory usage (Free vs Used including percentage)
- Total disk usage (Free vs Used including percentage)
- Top 5 processes by CPU usage
- Top 5 processes by memory usage
'''
import psutil 


def get_usage():
    usage = psutil.cpu_percent(interval=1)
    return usage

def get_mem_usage():
    memory = psutil.virtual_memory()
    mfree = memory[4]
    mused = memory[3]
    mpercentage = memory[2]
    return mfree, mused, mpercentage

def get_disk_space():
    space = psutil.disk_usage('/')
    dfree = space[2]
    dused = space[1]
    dpercentage = space[3]
    return dfree, dused, dpercentage

def get_top_processes(sort_by='value', limit=5):
    processes = []

    for i in psutil.proces_iter(['pid', 'name']):
        try:
            if sort_by == 'cpu':
                usage = proc.cpu_percent(interval=0.1)
            elif sort_by == 'mem'
                usage = proc.memory_info().rss
            else:
                print("invalid")
                return []
            
            processes.append({
                'pid': proc.info['pid'],
                'name': proc.info['name'],
                'usage': usage
            })
        except error as e
            print(f"{e}")
            continue
    processes.sort(key=lambda p: p['usage'], reverse=True)
    return processes[:limit]

if __name__ == '__main__':
    usage = get_usage()
    print(usage)

    musage = get_mem_usage()
    print(musage)

    space = get_disk_space()
    print(space)

    top5cpu = get_top_processes(sort_by='cpu')
    print(top5cpu)

    top5mem = get_top_processes(sort_by='mem')
    print(top5mem)
