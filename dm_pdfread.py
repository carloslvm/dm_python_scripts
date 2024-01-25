#!/usr/bin/python3

"""
This script allows to open en ebook using zathura as pdf
reader. This only works with PDF files, so do not try to
open epub file because it won't work.

If you use a tiling window manager like i3, the book will
open in full screen if you do not have anything opened beforehand.

The softwares required to use this script are dmenu and zathura,
which both can be downloaded for free online.

Author: Carlos
"""

import os

# dmenu look
text_color = "-nf \"#dfdfdf\" "
selector = "-sb \"#d9d31a\" "
f_selector = "-sf \"#000000\" "
misc = '-l 10 '
prompt_mes = "dmenu -p \"Select Book\" "

# Find Book to read
find_book = "find /home/carlos/Documents/Books/ -type f "

# dmenu commando
dmenu = prompt_mes + text_color + selector + f_selector + misc

# Adding quotes to dmenu's output
sed = 'sed -e \'s/.*/"&"/\' '

# Command to execute
command = find_book + ' | ' + dmenu + ' | ' + sed + ' | ' + "xargs zathura"

# Excute command
#print(command)
os.system(command)
