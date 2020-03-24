import sys, os
#-------------------------------------------------------------------------------
#functions to define
def split_path(path):
  full_path = path
  start, name = path.rsplit("\\", 1)
  #that makes sure that everything is spaced properly as well as adds double quotes to the names/paths
  return '"'+name.split(".")[0]+'"'+" "+'"'+path+'"'+" "+'"'+start+'"'

#this will be used later for running the second python script with the arguments after it
shortcut = ('python shortcuts.py')
#-------------------------------------------------------------------------------
#checks for itch.io directory to scan and askes for one if it is not detected
itchDIRfile = open('info\\itchDIR.txt', 'r+')
itchDIRcheck = itchDIRfile.readline()
if (itchDIRcheck == ""):
    itchDIR = input("copy and paste itch games directory ")
    itchDIRfile.write(itchDIR)
    itchDIRfile.close
else:
    itchDIR = itchDIRcheck
    print (itchDIR)
#-------------------------------------------------------------------------------
#checks for steam ID or askes for it if it is not detected
steamIDfile = open('info\\steamID.txt', 'r+')
steamIDcheck = steamIDfile.readline()
if (steamIDcheck == ""):
    steamIDpath = "C:\\Program Files (x86)\\Steam\\userdata"
    #opens steam user folder for users so they can copy and paste the numbers that represent their ID
    steamIDpath = os.path.realpath(steamIDpath)
    os.startfile(steamIDpath)
    steamID = str(input("copy and paste the numbers from the folder"))
    steamIDfile.write(steamID)
    steamIDfile.close()
else:
    steamID = steamIDcheck
    print (steamID)
#-------------------------------------------------------------------------------
# A bunch of variables that will be needed later
pathVDF = ('"'+"C:\\Program Files (x86)\\Steam\\userdata\\"+steamID+"\\config\\shortcuts.vdf"+'"'+" ")
name = "" #this gets defined later
path = ''# same
start = ""# same
hidden = " 0 "
allow_desktop_config = "1 "
allow_steam_overlay = "1 "
inVRLibrary = "0 " # 0 = no, 1 = yes
last_playtime = "0 " 
categories = ""
#this is a template in case I have to move stuff around
#extensions = (pathVDF+splitresult+" "+hidden+allow_desktop_config+allow_steam_overlay+inVRLibrary+last_playtime+categories)
#-------------------------------------------------------------------------------
#scans set directory for .exe files
for root, dirs, files in os.walk(itchDIR):
    for file in files:
        if file.endswith(".exe"):
             result = (os.path.join(root, file))
             splitresult = split_path(result)
             #------------------------------------------------------------------
             #it is important that it is at this indentation level or it will only set the first one
             extensions = (" "+pathVDF+splitresult+" "+'""'+" "+hidden+allow_desktop_config+allow_steam_overlay+inVRLibrary+last_playtime+categories)
             #This is when it uses the "shortcut" string thing I set earlier and it uses "extensions as the arguments"
             os.system(shortcut+extensions)
#--------------------------------------------------------------------------------
#just a couple of words for the user
print ("thanks for using my tool")
print ("glad I could help you automate some stuff")
close = input ("press enter to close")