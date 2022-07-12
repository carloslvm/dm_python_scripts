#!/usr/bin/env python3

"""
This script uses mpv and dmenu to play videos located
in the Videos directory. This script was tested only
on Linux system.

Select the video you want to play from the list shown
in dmenu, once you press enter video will be played
in fullscreen.

Usage:
    This script needs an argument, that argument is
    the path of the directory where videos are located.
    
    EXAMPLES:
        
        * python3 dm_video.py PATH
        * ./dm_video.py PATH

    The previous example shows two ways to execute the
    script in the terminal (command line). You can use
    the script as normal with dmenu but do not forget
    to add the PATH.

Author: Carlos Valdez

"""

import os
from sys import argv

# Dmenu appearance 
prompt_def = "dmenu -p "
prompt_mes = "\"Play Video\" "
text_color = "-nf \"#028DFE\" "
selector = "-sb \"#103962\" "
f_selector = "-sf \"#11FF00\" "
misc = '-l 20 '

# Getting Full Paths of videos
script, directory = argv
find_video = "find " + directory + " -name \"*.mp4\" "

# dmenu command
dmenu = prompt_def + prompt_mes + text_color + selector + f_selector + misc

# Formatting output
sed = 'sed -e \'s/.*/"&"/\' '

# Video Player
play_video = 'xargs mpv'

# Full command
command = find_video + '| ' + dmenu + '| ' + sed + '| ' + play_video

# Executing command
os.system(command)
