from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

thisfilespath = os.path.abspath(__file__)   #change working directory to this file's directory
dname = os.path.dirname(thisfilespath)
os.chdir(dname)

def encrypt(data):

    data = open(data, "rb")
    data = data.read()

    key = get_random_bytes(32)

    cipher = AES.new(key, AES.MODE_EAX)

    ciphertext, tag = cipher.encrypt_and_digest(data)


    with open("encrypted.bin", "wb") as f:
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
        print("Message decrypted!")
    except ValueError:
        print("Key incorrect or message corrupted")
    with open("decrypted.txt", "wb") as f:
        f.write(plaintext)

def main():
    print("You have started the AES cipher")
    print("Do you wish to [e]ncrypt or [d]ecrypt?")
    mode = input()
    if mode == "e":
        print("Encryption mode selected")
        print("Please input the file path:")
        print(encrypt(input()))
    elif mode == "d":
        print("Decryption mode selected")
        print("Please input the file path, then the associated hex key:")
        decrypt(data=input(), key=input())
    else:
        print("Wrong input! Exiting...")

if __name__ == '__main__':
    main()