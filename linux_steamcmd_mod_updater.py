#!/usr/bin/python3
import subprocess
import os
import sys
import logging as log

#config
steamcmddir = None
moddir = None
steamcmdlogdir = None
gameid = None
modlist = []

log.basicConfig(level=log.DEBUG, format='%(levelname)s: %(message)s')

#Step: Downloading
def modString():
        if not gameid:
                raise ValueError("Please provide a game id in the config at the start of the script.")
        mods = ""
        for i in modlist:
                mods += (" +workshop_download_item  " + gameid + " " + str(i))
        return mods

modstr = modString()
log.debug("Mod String: " + modstr)

if steamcmddir and moddir:
        if len(sys.argv) == 3:
                subprocess.check_call(steamcmddir + "/steamcmd.sh +force_install_dir " + moddir + " +login " + sys.argv[1] + " " + sys.argv[2] + modstr + " +quit", shell=True)
        else:
                log.info("You did not enter your username and password as start arguments. \n Continuing with anonymous login...\n")
                subprocess.check_call(steamcmddir + "/steamcmd.sh +force_install_dir " + moddir + " +login anonymous" + modstr + " +quit", shell=True)
else:
        log.error("Please fill out the config at the start of the script.")

#Step: Deleting logs - UNTESTED
logfiles = ["configstore_log.txt", "appinfo_log.txt", "content_log.txt", "connection_log.txt", "workshop_log.txt"]

if steamcmdlogdir:
        for i in logfiles:
                path = steamcmdlogdir + i
                if os.path.exists(path):
                        os.remove(path)
                else:
                        log.error("Path: " + path + " Does not exist.")
else:
        log.error("steamcmdlogdir was not set in config. Logs will not be deleted.\n If you have provided login data, it will be in these logs.")       #TODO: Conclusiveness of this solution has not been proven yet.

#Step: Copying and renaming files into moddir - UNTESTED
subprocess.check_call(r"cd "+ moddir +"/steamapps/workshop/content/" + gameid + " && find . -depth -type f -exec rename -f 's/(.*)\/([^\/]*)/$1\/\L$2/' {} \; && cp -u -r ./ ../../../..", shell=True)