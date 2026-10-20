from Crypto.Cipher import AES   #installed via pycryptodome package
from Crypto.Random import get_random_bytes
import tarfile
import os
import argparse
#TODO MemoryError on decrypt L70
#TODO optional naming arg
#Note: There is no debugger present, handling debugging with print statements is really tedious.

thisfilespath = os.path.abspath(__file__)   #change working directory to this file's directory - why again?
dname = os.path.dirname(thisfilespath)
os.chdir(dname)
#argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("mode",choices=["e", "encrypt", "d", "decrypt"], help="select encryption or decryption mode")
parser.add_argument("path", help="input your file/directory path in quotation marks")
parser.add_argument("key",nargs="?", help="a key to your encrypted file in hex format")
parser.add_argument("-o", "--overwrite", action="store_true")   #stores in args.overwrite
args = parser.parse_args()

def archive(source):
    os.chdir(source)
    filename = "encrypted.tar"
    if os.path.isfile(filename):    #duplicate handling
        if not args.overwrite:   
            i = input(filename + " already exists. Overwrite existing file? [y/n]\n")
            if i == "y":
                os.remove(filename)
            elif i == "n":
                filename = input("What should your encrypted file be called?")
                filename = filename + ".tar"
            else:
                print("invalid input. Exiting..")
                return 1
        else:
            os.remove(filename)
    #main part of function
    print("archiving...")
    with tarfile.open(filename, "w") as tar:
        tar.add(source, arcname=os.path.basename(source))
    return filename
            
def dearchive(file):
    os.chdir(os.path.dirname(file))
    if not file:
        print("No file given")
    tar = tarfile.open(file)
    tar.extractall()
    tar.close()

def encrypt(data):
    print("encrypting...")
    name = data
    data = open(data, "rb")
    data = data.read()
    key = get_random_bytes(32)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)   
    with open(name, "wb") as f:
        f.write(tag)
        f.write(cipher.nonce)
        f.write(ciphertext)
    return key.hex()

def decrypt(data,key):
    key = bytes.fromhex(key)
    with open(data, "rb") as f:
        tag = f.read(16)
        nonce = f.read(16)
        ciphertext = f.read()
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        print("decrypted!")
    except ValueError:
        print("Key incorrect or file corrupted")
    with open(data, "wb") as f:
        f.write(plaintext)

def main():
    path = args.path
    if args.mode == ("e" or "encrypt"):
        n = archive(path)
        print("Your hex key:" + encrypt(n))
        del n
    elif args.mode == ("d" or "decrypt") and args.key:
        decrypt(data=path, key=args.key)
        dearchive(path)
        print("Decryption Successful")
    else:
        print("No hex key supplied. Exiting...")

if __name__ == '__main__':
    main()