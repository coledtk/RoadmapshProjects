#https://gist.githubusercontent.com/kamranahmedse/e66c3b9ea89a1a030d3b739eeeef22d0/raw/77fb3ac837a73c4f0206e78a236d885590b7ae35/nginx-access.log
import os

location = r'C:\Users\cdetrick\OneDrive - Sirius XM Radio Inc\Desktop\RoadmapshProjects\RoadmapshProjects\analyze_Nginx'
for f in os.listdir(location):
    if f == 'nginx.log':
        fl = open(os.path.join(location, 'nginx.log'), "r")
        print(fl.read())

