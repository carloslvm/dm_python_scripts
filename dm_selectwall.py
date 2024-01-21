#!/usr/bin/python3

"""

This script allows you to set your wallpaper using feh and dmenu. It is
required to have dmenu and feh installed in your system.

This script does not required any kind of argument and it was successfully
tested on Linux Debian 11 Bullseye. Make sure to save this script in one
of the directories located in your PATH variable, so dmenu can execute it.

"""

import os

# dmenu appearance
prompt_def = "dmenu -p "
prompt_mes = "\"Select Wallpaper\" "
text_color = "-nf \"#c8c8c8\" "
selector = "-sb \"#c8c8c8\" "
f_selector = "-sf \"#00007f\" "
misc = '-l 10 '

# Show files in Wallpapers directory
show_wallpapers = 'find /home/carlos/Pictures/Wallpapers/ -type f '

# dmenu command
dmenu = prompt_def + prompt_mes + text_color + selector + f_selector + misc

# Assigning wallpaper with feh
feh = "xargs feh --bg-scale "

# Adding quotes to dmenu's output
sed = 'sed -e \'s/.*/"&"/\' '

# Command to execute
command = show_wallpapers + '| ' + dmenu + '| ' + sed + '| ' + feh

# Excuting command
os.system(command)
