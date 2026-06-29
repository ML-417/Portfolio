#!/usr/bin/python3
import subprocess
import os
import sys
import logging as log

#config
steamcmddir = None
moddir = None
modlist = []

#TODO: call steamcmd.sh with arguments instead of the script. DELETE LOGIN FILES!!! Implement cpmods.sh into script without the use of external bash scripts.

log.basicConfig(level=log.INFO, format='%(levelname)s: %(message)s')
if steamcmddir and moddir:
        nick, passwd = sys.argv[1:0], sys.argv[1:1]
        if nick and passwd:
                subprocess.call(steamcmddir + "/steamcmd.sh +force_install_dir " + moddir + "+login " + nick + " " + passwd)
        else:
                print("You did not enter your username and password as start arguments. \n Continuing with anonymous login...")
                subprocess.call(steamcmddir + "/steamcmd.sh +force_install_dir " + moddir + "+login anonymous")
        subprocess.check_call()         #wait function for called process
else:
        print("Please fill out the config at the start of the script.")
subprocess.run("a3updatecomponents/cpmods.sh",shell=True)