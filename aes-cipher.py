from Crypto.Cipher import AES   #installed via pycryptodome package
from Crypto.Random import get_random_bytes
import tarfile
import os
import argparse

#TODO edit main function for args, immediate steps are in comments.
thisfilespath = os.path.abspath(__file__)   #change working directory to this file's directory - why again?
dname = os.path.dirname(thisfilespath)
os.chdir(dname)

def archive(source, filename:str):
    os.chdir(source)
    if not filename:
        filename = "encrypted"
        print("no file name given, using default.")
        
    filename = filename + ".tar"
    if os.path.isfile(filename):
        print(filename + " already exists.")
    else:
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
        print("Key incorrect or message corrupted")
    with open(data, "wb") as f:
        f.write(plaintext)

def main():
    parser = argparse.ArgumentParser()  #does this have help already?
    parser.add_argument("mode",choices=["e", "encrypt", "d", "decrypt"], help="select encryption or decryption mode")
    parser.add_argument("path", help="always a path")   #change this help
    parser.add_argument("key", help="a key to your encrypted file in hex format")   #make this not always necessary
    args = parser.parse_args()
    if args.mode == "e" or "encrypt":
        t = args.path
        n = input("What should your encrypted file be called?\n")   #remove this.
        n = archive(t,n)
        print(encrypt(n))
        del t,n
    elif args.mode == "d" or "decrypt":
        print("Decryption mode selected")
        print("Please input the file path you want to decrypt.")
        t = input()
        print("What is your hex key?")
        decrypt(data= t, key=input())
        dearchive(t)
        del t
        print("Decryption Successful")
    else:
        print("Wrong input! Exiting...")

if __name__ == '__main__':
    main()