'''Top 5 IP addresses with the most requests
Top 5 most requested paths
Top 5 response status codes
Top 5 user agents
'''
#https://gist.githubusercontent.com/kamranahmedse/e66c3b9ea89a1a030d3b739eeeef22d0/raw/77fb3ac837a73c4f0206e78a236d885590b7ae35/nginx-access.log
import os
import re

location = r'C:\Users\cdetrick\OneDrive - Sirius XM Radio Inc\Desktop\RoadmapshProjects\RoadmapshProjects\analyze_Nginx'
for filename in os.listdir(location):
    if filename == 'nginx.log':
        f = open(os.path.join(location, 'nginx.log'), "r")
        data = f.read()

def get_top5_IP(data):
    x = ''.join(re.findall("[0-9]{3}[.][(0-9]{3}|{2})]{3}"))
    print(x)