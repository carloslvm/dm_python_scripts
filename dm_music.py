#!/usr/bin/env python3

"""
The main idea of this script is to be able to play music located in
the Music directory using mpv as backend and dmenu as music selector,
so you will need to install mpv and dmenu to make it work.

Music will be played in the background. If you need to stop it, you
can use the dm_kill script.

Author: Carlos Valdez

"""

import os

# dmenu looking
prompt_def= "dmenu -p "
prompt_mes= '"Play Music" '
text_color = "-nf \"#939393\" "
selector = '-sb "#034102" '
f_selector = '-sf "#0DE509" -l 20 '

# Getting mp3 full paths
find_mp3 = 'find /home/carlos/Music/ -name "*.mp3" '

# dmenu command
dmenu = prompt_def + prompt_mes+ text_color + selector + f_selector

# Formatting dmenu output (adding " to dmenu's output)
sed = 'sed -e \'s/.*/"&"/\' '

# Music Player
play = 'xargs mpv'

# Full command
command = find_mp3 + '| ' + dmenu + '| ' + sed + '| ' + play

# Executing command
os.system(command)

#NICE
