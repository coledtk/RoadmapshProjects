#!/bin/sh/bash

top -bn1 | grep 'CPU(s)' | \
    awk '{print "CPU Usage: " 100 - *8 "%"}'
