#!/usr/bin/env python3

"""
This script uses mpv and dmenu to play videos located
in the Videos directory. This script was tested only
on Linux system.

Select the video you want to play from the list shown
in dmenu, once you press enter video will be played
in fullscreen.

Author: Carlos Valdez

"""

import os

# Dmenu appearance 
prompt_def = "dmenu -p "
prompt_mes = "\"Play Video\" "
text_color = "-nf \"#028DFE\" "
selector = "-sb \"#103962\" "
f_selector = "-sf \"#11FF00\" "
misc = '-l 20 '
pipe = '| '

# Getting Full Paths of videos
find_video = "find /home/carlos/Videos/ -name \"*.mp4\" "

# dmenu command
dmenu = prompt_def + prompt_mes + text_color + selector + f_selector + misc

# Formatting output
sed = 'sed -e \'s/.*/"&"/\' '

# Video Player
play_video = 'xargs mpv'

# Full command
command = find_video + '| ' + dmenu + '| ' + sed + '| ' + play_video
#print(command)

# Executing command
os.system(command)
