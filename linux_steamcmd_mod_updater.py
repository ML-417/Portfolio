#!/usr/bin/python3
import subprocess
import os
import sys
import logging as log

#config
steamcmddir = None
moddir = None
gameid = "107410"
modlist = []

#TODO: call steamcmd.sh with arguments instead of the script. DELETE LOGIN FILES!!! Implement cpmods.sh into script without the use of external bash scripts.

log.basicConfig(level=log.INFO, format='%(levelname)s: %(message)s')

def modString():
        mods = ""
        for i in modlist:
                mods += (" +workshop_download_item  " + gameid + " " + str(i))
        return mods

modstr = str(modString())
log.info("Mod String: " + modstr)

if steamcmddir and moddir:
        if len(sys.argv) == 3:
                subprocess.check_call(steamcmddir + "/steamcmd.sh +force_install_dir " + moddir + " +login " + sys.argv[1] + " " + sys.argv[2] + modstr + " +quit", shell=True)
        else:
                print("You did not enter your username and password as start arguments. \n Continuing with anonymous login...")
                subprocess.check_call(steamcmddir + "/steamcmd.sh +force_install_dir " + moddir + " +login anonymous" + modstr + " +quit", shell=True)
#       subprocess.check_call()         #wait function for called process
else:
        print("Please fill out the config at the start of the script.")
#subprocess.run("a3updatecomponents/cpmods.sh",shell=True)