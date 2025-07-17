#!/bin/bash

LOCAL_DIR=./dist
REMOTE_USER=ec2-user
REMOTE_HOST=your-ec2-ip
REMOTE_PATH=/var/www/my-site
KEY=your-key.pem

rsync -avz -e "ssh -i $KEY" $LOCAL_DIR/ $REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH
