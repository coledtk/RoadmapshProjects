#!/bin/bash
set -euo pipefail
exec >> /tmp/fake-load.log 2>&1

# stress 1 core for 5 seconds
stress --cpu 1 --timeout 5

# write 10M
dd if=/dev/urandom of=/tmp/fakefile bs=1M count=10 status=none
rm -f /tmp/fakefile

