import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ.,? "   #what characters to use? This can be expanded.

def keyGen(chars):
    chars = list(chars)
    random.shuffle(chars)
    return "".join(chars)

def encrypt(plaintext):
    key = keyGen(chars)
    keyMap = dict(zip(chars, key))
    return ''.join(keyMap.get(c.upper(), c) for c in plaintext), key

def decrypt(encrtext, key):
    keyMap = dict(zip(key, chars))
    return ''.join(keyMap.get(c.upper(), c) for c in encrtext)

def main():
    print("You have started the substitution cipher")
    print("Do you wish to [e]ncrypt or [d]ecrypt?")
    mode = input()
    if mode == "e":
        print("Encryption mode selected")
        print("Please input the text you want to encrypt:")
        plaintext = input()
        encrtext, key = encrypt(plaintext)
        print("Your encrypted text: " + encrtext) 
        print("The key for decrypting it: " + key)
        print("Please note, that this encryption method isn't very sophisticated.")
    elif mode == "d":
        print("Decryption mode selected")
        print("Please input the encrypted text:")
        encrtext = input()
        print("Please input the right key for decryption:")
        key = input()
        print("Your decrypted text:\n" + decrypt(encrtext, key))

    else:
        print("Wrong input! Exiting...")

if __name__ == '__main__':
    main()