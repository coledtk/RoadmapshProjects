''' query server for:
- Total CPU usage.
- Total memory usage (Free vs Used including percentage).
- Total disk usage (Free vs Used including percentage).
- Top 5 processes by CPU usage.
- Top 5 processes by memory usage.
'''
import psutil 

# formats the return value (bytes) into correct unit of measurement
def format_bytes(size):
    for unit in ['B', "KB", 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{round(size, 2)} {unit}"
        size /= 1024

# waits 1 second, then measures CPU usage over that time, returns a float.
def get_usage():
    usage = psutil.cpu_percent(interval=1)
    return usage


# get all virtual memory information then parses for attributes.
def get_mem_usage():
    memory = psutil.virtual_memory()
    mfree = format_bytes(memory.available)
    mused = format_bytes(memory.used)
    mpercentage = memory.percent
    return mfree, mused, mpercentage


# get all disk information then parses for attributes.
def get_disk_space():
    space = psutil.disk_usage('/')
    dfree = format_bytes(space.free)
    dused = format_bytes(space.used)
    dpercentage = space.percent
    return dfree, dused, dpercentage

# grabs running system processes
def get_top_processes(sort_by='cpu', limit=5):
    processes = []
    # grabs running system processes
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # determines if sorting by cpu or ram usage.
            if sort_by == 'cpu':
                usage = proc.cpu_percent(interval=0.1)
            elif sort_by == 'mem':
                usage = proc.memory_info().rss # resident set size = how much ram the proc is using
            else:
                print("invalid sort option")
                return []
            # returns the top 5
            processes.append({
                'pid': proc.info['pid'],
                'name': proc.info['name'],
                'usage': usage
            })
        except Exception as e:
            print(f"Error: {e}")
            continue
            # sorts based on either cpu or ram usage.
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
