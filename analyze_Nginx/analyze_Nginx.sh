#!/bin/bash
#https://gist.githubusercontent.com/kamranahmedse/e66c3b9ea89a1a030d3b739eeeef22d0/raw/77fb3ac837a73c4f0206e78a236d885590b7ae35/nginx-access.log
# https://www.digitalocean.com/community/tutorials/awk-command-linux-unix#printing-all-lines-in-a-file

# top 5 ip addresses.
awk '{print $1}' nginx.log | sort | uniq -c | sort -nr | head -5
# top 5 requested paths.
awk -F\" '{print $2}' nginx.log | awk '{print $2}' | sort | uniq -c | sort -nr | head -5
# top 5 status codes.
awk -F\" '{print $3}' nginx.log | awk '{print $1}' | sort | uniq -c | sort -nr | head -5
# top 5 user agents.
awk -F\" '{print $6}' nginx.log | sort | uniq -c | sort -nr | head -5

