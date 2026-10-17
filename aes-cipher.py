from Crypto.Cipher import AES   #installed via pycryptodome package
from Crypto.Random import get_random_bytes
import tarfile
import os
#TODO Last: make this a script runnable with args and help
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
    print("You have started the AES cipher")
    print("Do you wish to [e]ncrypt or [d]ecrypt?")
    mode = input()
    if mode == "e":
        print("Encryption mode selected")
        t = input("Please input the path you want to encrypt:\n")
        n = input("What should your encrypted file be called?\n")
        n = archive(t,n)
        print(encrypt(n))
        del t,n
    elif mode == "d":
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