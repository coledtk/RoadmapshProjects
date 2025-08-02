#!/bin/bash
rsync -avz -e "ssh -i <ssh-key-location>" <targetFolder> ec2-user@<ec2-ip>:/home/ec2-user/destinationFolder/
