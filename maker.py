#


import sys, subprocess
result = ("")
dir1 = input ('what is your itch.io folder (I.E. C:\\Users\\user\\itch\\games)')
file1 = open('apps.txt','w')

import os
for root, dirs, files in os.walk(dir1):
    for file in files:
        if file.endswith(".exe"):
             result = (os.path.join(root, file))
             file1.write (result + '\n')
             
file1.close()

pathVDF = ("C:\\Program Files (x86)\\Steam\\userdata\\UserID\\config\\shortcuts.vdf ")
name = ""
path = ''
start = ""
hidden = "0 "
allow_desktop_config = "1 "
allow_steam_overlay = "1 "
inVRLibrary = ""
last_playtime = "0 "
categories = ""

#this bit usually asks what the name and paths are

#name = input ("what is the name of the game")
#path = input ("paste the entire path to EXE(I.E. C:\\Users\\user\\games\\game.exe)")
#start = input ("paste directory with exe in it(I.E. C:\\Users\\user\\games)")
#inVRLibrary = input ("if it is a VR game, press 1, otherwise press 0")
#categories = input ("are there and cagetorgies you want the game in(I.E. RTS, FPS, simulation)")


#--------------------------------------------------------------------------------

def split_path(path):
  full_path = path
  path_to_exe, game_name = path.rsplit("\\", 1)
  return full_path, path_to_exe, name.split(".")[0]
  path_data = split_path(path)
#splits full path into smaller bits 
#--------------------------------------------------------------------------------

LineToRead = 1
counter = 0
amount = int(input("number of installed itch games"))
file = open("apps.txt", 'r')
print (" ")
while (counter < amount):
#checks if the line is empty and moves the script forward if it is
    if (file.readline(LineToRead) == ""):
            counter += 1
#reads what the line is and splits it
    else:
            file.readline(LineToRead)
            pathedit = (file.read())
            exstension = splitpath(pathedit)
            LineToRead = LineToRead + 1
file.close()
#reads each line
#-------------------------------------------------------------------------------

extensions = (pathVDF, name, " ",path, " ",start, " ", hidden, allow_desktop_config, allow_steam_overlay, inVRLibrary," ", last_playtime, categories)
close = input ("press enter to close")
if (close == ""):
    subprocess.call(['cleanup.bat' 'r'])
