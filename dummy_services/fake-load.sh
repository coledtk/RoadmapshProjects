#!/bin/bash

# yes to /dev/null set PID
(yes > /dev/null &) && PID = $!

# wait 5 seconds
sleep

# write 10m to /tmp 
dd if=/dev/urandom of=/tmp/dummyservice bs=1m count=10 status=none

# remove file
rm -f /tmp/dummyservice

