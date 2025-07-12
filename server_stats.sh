#!/bin/bash
# top command, flag for running in batch mode (returns text instead of an interactive display), -n1 (returns once, like a snapshot)
# | pipe to grep, looks for line in top command that says 'CPU(s)'
# \ tells the shell that the script continues on the next line.
# awk is a text processing tool, tells shell to print "pattern"
# it grabs the pattern 'SPU Usage:' and then subtracts 100 from the idle CPU %, $8 = 8th field in the grep output.
# then just prints a % sign
top -bn1 | grep 'CPU(s)' | \ 
    awk '{print "CPU Usage: " 100 - $8 "%"}'
