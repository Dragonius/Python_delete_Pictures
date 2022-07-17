#!/usr/bin/env python3

import sys
import os
import imageio
import numpy as np
from PIL import Image


#print("Files and directories in '", path, "' :")

# print the list
#print(dir_list)


def main():
    path = sys.argv[-1]
    if (path==""):
        os._exit(0)

    dir_list = os.listdir(path)
    for filename in os.listdir(path):
        #print(path)
        if filename.endswith(".jpg"):
        #    print(filename)
            pathfilename = path + filename
        #    print(pathfilename)

        #print(pathfilename)
        try:
            im = Image.load(pathfilename)
            im.verify() #I perform also verify, don't know if he sees other types o defects
            im.close() #reload is necessary in my case
            im = Image.load(pathfilename)
            im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
            im.close()
        except:
        #manage excetions here
            print("Coultn't open image file on im")
            #sys.exit(0)

        f = imageio.imread(pathfilename, as_gray=True)
        #print(pathfilename)
        try:
            #print(pathfilename)
            imageio.verify(f)
        # do stuff
        except IOError:
        # filename not an image file
            print("File is not image, IO error")
            sys.exit(0)

        def img_estim(img, thrshld):
            is_light = np.mean(img) > thrshld
            #print(np.mean(img))
            #return 'light' if is_light else os.remove(filename)
            if is_light == 0:
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

