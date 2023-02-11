#!/usr/bin/python3

"""
This was created to kill processes on Linux system using dmenu.
Please use it with caution.

Processes will be shown on dmenu, search or type the process
you need to kill and once you press enter that process will
stop running.

This script needs one argument to be executed, that argument
will determine whether to kill, stop or resume the process.

EXAMPLES:

    * ./dm_kill.py killing
    * ./dm_kill.py stop
    * ./dm_kill.py cont

I used ps command to display processes so it is recommended
to take a look at its documentation in order to learn how
to identify the status of a process.


Author: Carlos Valdez

"""

import os
from sys import argv

# dmenu appereance
prompt_def = "dmenu -p "
prompt_mes = '"Kill" '
text_color = "-nf \"#ADADAC\" "
selector = '-sb "#7A0000" '
f_selector = '-sf "#F79707" '
misc = "-b -l 20 " # Appears at the bottom of screen, 20 lines.

# System processes
proc = "ps -ex "

# dmenu command
dmenu = prompt_def + prompt_mes + text_color + selector + f_selector

# Getting Process ID
proc_id = "cut --delimiter=' ' -f 1,2 "

# Kill process
option = argv[1]

if option == 'killing': 
    killing = "xargs kill" # Kill the process (no possible to resume)
elif option == 'cont':
    killing = "xargs kill -18" # Resume process
elif option == 'stop':
    killing = "xargs kill -19" # Stop process

# Full command
command = proc + '| ' + dmenu + misc + '| ' + proc_id + '| ' + killing

#Execute command
os.system(command)
