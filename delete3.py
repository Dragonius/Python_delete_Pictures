#!/usr/bin/env python3

import sys
import os
#import imageio
#image io got updated and they building next to next v2 and v3 brances.
#and there are problems with python3.6 <> python3.7 versions
if sys.version_info < (3, 7):
    import imageio
else:
    import imageio.v2 as imageio

import numpy as np
from PIL import Image


#print("Files and directories in '", path, "' :")

# print the list
#print(dir_list)
#ask for arguments for directory, ifn't given any , exit

def main():
    path = sys.argv[-1]
    if (path==""):
        os._exit(0)

    dir_list = os.listdir(path)
    #sort file list, as dir_list cant be a mess order
    dir_list.sort()
    #print(dir_list)
    for filename in os.listdir(path):
        #print(path)
        if filename.endswith(".jpg"):
            #print(filename)
            #print(path)
            pathfilename = path + filename
            #print(pathfilename)

        #print(pathfilename)
        try:
            img = Image.open(pathfilename)
            img.verify() #I perform also verify, don't know if he sees other types o defects
            img.close() #reload is necessary in my case
#            img = Image.open(pathfilename)
#            img.transpose(PIL.Image.FLIP_LEFT_RIGHT)
#            img.close()
        except:
        #manage excetions here:
        #dont quit, because we goind dir of files,
            print("Couldtn't open image file: ", pathfilename)
            #sys.exit(0)
            #print(pathfilename)

        f = imageio.imread(pathfilename, as_gray=True)


        #Imageio Verify is broken and its not coming back
        #print(pathfilename)
#        try:
            #print(pathfilename)
#            imageio.verify(f)
        # do stuff
#        except IOError:
#        # filename not an image file
#            print("File is not image, IO error")
#            sys.exit(0)

        def img_estim(img, thrshld):
            is_light = np.mean(img) > thrshld
            #print(np.mean(img))
            #return 'light' if is_light else os.remove(filename)
            if is_light == 0:
                #dont print anything, just Delete
                os.remove(pathfilename)

        img_estim(f, 40)
        #print(img_estim(f, 40))
        #print

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
