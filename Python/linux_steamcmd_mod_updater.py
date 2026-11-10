#!/usr/bin/python3
import subprocess
import os
import sys
import logging as log
########config##########
gameid = None
moddir = None
steamcmddir = None
steamcmdlogdir = None
modupdate = False
modlinking = False   #Needs lndir to work
modcleaner = False
modrelpth = None  #Relative path from your start script to mod folder
modstrf = False       #Prints a string for the "mods=" section of your start script. Needs modrelpth.
modlist = []         #List of workshop item ids
########################

log.basicConfig(level=log.INFO, format="%(levelname)s: %(message)s")


def modString(gameid,modlist):
    if not gameid:
        raise ValueError("Please provide a gameid in the config at the start of the script.")
    mods = ""
    if modlist:
        for i in modlist:
            mods += (" +workshop_download_item  " + gameid + " " + str(i))
    else: log.info("modlist is empty.")
    return mods

def runSteamcmd(steamcmddir, moddir, modstr):
    print("Please enter your steam login data or continue anonymous")
    uname = input("Username: ")
    pword = input("Password: ")
    if (len(uname) + len(pword)) > 1:
        subprocess.check_call(steamcmddir + "/steamcmd.sh +force_install_dir " + moddir + " +login " + uname + " " + pword + modstr + " +quit", shell=True)
    else:
        log.info("You did not enter your username and password. \n Continuing with anonymous login...\n")
        subprocess.check_call(steamcmddir + "/steamcmd.sh +force_install_dir " + moddir + " +login anonymous" + modstr + " +quit", shell=True)

def delSteamcmdLogs(steamcmdlogdir):
    logfiles = ["configstore_log.txt", "appinfo_log.txt", "content_log.txt", "connection_log.txt", "workshop_log.txt"]    #This shouldn't change.
    for i in logfiles:
        path = steamcmdlogdir + "/"+ i
        if os.path.exists(path):
            os.remove(path)
        else:
            log.error("Path: " + path + " Does not exist.")

def linkMods(moddir, gameid):
    log.info("The next step might require you to install xutils-dev, as it uses lndir.")
    subprocess.check_call("lndir -silent" + moddir + "/steamapps/workshop/content/" + gameid + " " + moddir, shell=True)
    subprocess.check_call("cd "+ moddir + r" && find . -maxdepth 4 -type l -exec rename -f 's/(.*)\/([^\/]*)/$1\/\L$2/' {} \;", shell=True)

def cleanMods(modinstalldir, modlist, moddir):
    dellst = []
    templst = os.scandir(modinstalldir)
    for i in templst:
        if i.is_dir() and i not in modlist:
            dellst.append(i.name)
    if len(dellst) > 0:
        print("Do you want to delete following folders from " + modinstalldir + " ? [y/n]")
        for i in dellst:
            print(i)
        if input() == "y":
            for i in dellst:
                subprocess.check_call("cd " + modinstalldir + " && rm -rf " + i + "/", shell=True)
                subprocess.check_call("cd " + moddir + " && rm -rf " + i + "/", shell=True)
            print("Deleted " + str(len(dellst)) + " items successfully")
    else: print ("No files are flagged for deletion.")
    templst.close()

def formattedModStr(modlist, modrelpth):
    tempstr = ""
    for i in modlist:
        tempstr += (modrelpth + i + ";")
    print ("modtxt string:\n" + tempstr)

def main():
    if not (gameid and moddir):
        print("You did not fill the top two entries of the config, which are essential for this script to run.")
        sys.exit()
    modinstalldir = moddir + "/steamapps/workshop/content/" + gameid

    modstr = modString(gameid=gameid,modlist=modlist)
    log.debug("Mod String: " + modstr)
    if steamcmddir and modupdate:
        runSteamcmd(steamcmddir=steamcmddir, moddir=moddir, modstr=modstr)
    if steamcmdlogdir:
        delSteamcmdLogs(steamcmdlogdir=steamcmdlogdir)
    elif not (steamcmdlogdir and modupdate):
        log.warning("steamcmdlogdir was not set in config. Logs will not be deleted.\n If you have provided login data, it will be in the logs.")
    if modlinking:
        linkMods(moddir=moddir, gameid=gameid)
    if modcleaner:
        cleanMods(modinstalldir=modinstalldir, modlist=modlist, moddir=moddir)
    if modstrf:
        formattedModStr(modlist=modlist, modrelpth=modrelpth)
if __name__ == "__main__":
    main()