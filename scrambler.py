import os
path = r""
files = os.listdir(path)

for i in files:
    os.rename(path + "/" + i, path + "/" + str(hash(os.urandom(8)))[2:])