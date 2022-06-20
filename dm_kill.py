#!/usr/bin/python3

"""
This was created to kill processes on Linux system using dmenu.
Please use it with caution.

Processes will be shown on dmenu, search or type the process
you need to kill and once you press enter that process will
stop running.

Author: Carlos Valdez

"""

import os

# dmenu appereance
prompt_def = "dmenu -p "
prompt_mes = '"Kill" '
text_color = "-nf \"#ADADAC\" "
selector = '-sb "#7A0000" '
f_selector = '-sf "#F79707" '
misc = "-b -l 20 " # Appears at the bottom of screen, 20 lines.

# System processes
proc = "ps -faux "

# dmenu command
dmenu = prompt_def + prompt_mes + text_color + selector + f_selector

# Getting Process ID
proc_id = "cut --delimiter=' ' -f 4 "

# Kill process
kill = "xargs kill"

# Full command
command = proc + '| ' + dmenu + misc + '| ' + proc_id + '| ' + kill

#Execute command
os.system(command)
