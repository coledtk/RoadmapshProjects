'''Top 5 IP addresses with the most requests
Top 5 most requested paths
Top 5 response status codes
Top 5 user agents
'''
#https://gist.githubusercontent.com/kamranahmedse/e66c3b9ea89a1a030d3b739eeeef22d0/raw/77fb3ac837a73c4f0206e78a236d885590b7ae35/nginx-access.log
import re
from collections import Counter

def parse_log(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    ip_pattern = re.compile(r'^\d{1,3}(?:\.\d{1,3}){3}')
    path_pattern = re.compile(r'\"[A-Z]+ (.*?) HTTP/')
    status_pattern = re.compile(r'\" \d{3} ')
    user_agent_pattern = re.compile(r'\" \"(.*?)\"$')

    ips = []
    paths = []
    statuses = []
    user_agents = []

    for line in lines:
        if m := ip_pattern.search(line):
            ips.append(m.group())
        if m := path_pattern.search(line):
            paths.append(m.group(1))
        if m := status_pattern.search(line):
            statuses.append(m.group().strip('" '))
        if m := user_agent_pattern.search(line):
            user_agents.append(m.group(1))

    return {
        'ips': Counter(ips).most_common(5),
        'paths': Counter(paths).most_common(5),
        'statuses': Counter(statuses).most_common(5),
        'user_agents': Counter(user_agents).most_common(5),
    }

def main():
    log_path = r'enter_your_path_to_logs.log'
    top = parse_log(log_path)
    for k, v in top.items():
        print(f"\nTop 5 {k.replace('_', ' ')}:")
        for item, count in v:
            print(f"{item} - {count}")

if __name__ == '__main__':
    main()