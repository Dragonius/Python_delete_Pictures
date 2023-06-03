import sys
import os
#import imageio
#image io got updated and they building next to next v2 and v3 brances.
if sys.version_info < (3, 7):
    import imageio
else:
    import imageio.v2 as imageio

import numpy as np
from PIL import Image


#print("Files and directories in '", path, "' :")

# print the list
print("print list that show filenames")
print()
#ask for arguments for directory, ifn't given any , exit
path = "/home/kayttaja/Lataukset/Git/Python_delete_Pictures/test_files/"
dir_list = os.listdir(path)
print(dir_list)

print()
print("Full dir with name ")
print()
for filename in os.listdir(path):
    #print(path)
    if filename.endswith(".jpg"):
        #print(filename)
        #print(path)
        pathfilename = path + filename
        print(pathfilename)

print()
print("alternative style")
print()

data_len=len(dir_list)
data_out = 0
if (data_len > -1):
    while (data_len > data_out):
        
        print(dir_list[data_out])
        data_out= data_out+1
        #wait(100)


