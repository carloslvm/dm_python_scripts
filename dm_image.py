#!/usr/bin/python3

"""
This script requires dmenu and sxiv to work properly. This script was successfully
tested on Linux system (Debian Bullseye).

USAGE:
    1. Save the script in a directory registered in your PATH variable.
    2. Make sure it has execution permissions.
    3. Open dmenu type the name of script with one of its arguments:
        1. First argument available is "directory"
        2. Second argument available is "file"

EXAMPLE:
    This example terminal based to test the script works properly:
    ./dm_image.py directory
    ./dm_image.py file

    If you want to execute it from the dmenu, just omit the "./" characters:
    dm_image.py directory
    dm_image.py file

Author: Carlos
"""
import os
from sys import argv

#dmenu looking set up
prompt_def = 'dmenu -p'
text_color = "-nf \"#ADADAC\" "
selector = '-sb "#7A0000" '
f_selector = '-sf "#F79707" '
misc = "-l 10" # Appears at top of the screen, 10 lines

# Arguments will be "directory" and "file"
argument = argv[1]
if argument == 'directory':
    prompt_mes = ' Directory '
    directories = 'find /home/carlos/Pictures/ -type d '
elif argument == 'file':
    prompt_mes = ' Image '
    find_image = 'find /home/carlos/Pictures/ -name "*[!xfc]" '

# dmenu command
dmenu = prompt_def + prompt_mes + text_color + selector + f_selector + misc

# Viewing images
if argument == 'directory':
    command = directories + '| ' + dmenu + ' | ' + 'xargs sxiv -t'
elif argument == 'file':
    command = find_image + '| ' + dmenu + ' | ' + 'xargs sxiv'

# Excute command
os.system(command)

