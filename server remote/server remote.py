import logging as log
from paramiko import SSHClient

log.basicConfig(level=log.INFO, format='%(levelname)s: %(message)s')

def getConInfo():
    uname, password, keyloc, host, port, pname = [None] * 6
    print("Please enter your basic connection information")
    print("Username:")
    uname = input()
    print("Are you using a [p]assword or [k]ey file? [p/k]")
    answer = input()
    if answer == "k":
        print("Pass key location:")
        keyloc = input()
    print("Password:")
    password = input()
    print("Host name:")
    host = input()
    print("Port:")
    port = input()
    print("Do you want to save this information? [y/n]")
    answer = input().lower()
    if answer == "y":
        print("Under which name do you want to save it?")
        pname = input()
    log.info(str((uname, password, keyloc, host, port, pname)))
    return uname, password, keyloc, host, port, pname

def main():
    getConInfo()
    #SSHClient.connect(hostname=host, port=port, username=uname, password=password, key_filename=keyloc)

if __name__ == '__main__':
    main()