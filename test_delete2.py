#!/usr/bin/env python3

import sys
import os
import imageio
import numpy as np
from PIL import Image

def main():
    #filename = "./test_files/Clouds_test.jpg"
    filename = sys.argv[-1]
    print(filename)

    try:
        im = Image.load(filename)
        print("im loaded")
        im.verify() #I perform also verify, don't know if he sees other types o defects
        print("im verify")
        im.close() #reload is necessary in my case
        print("im close")
        im = Image.load(filename)
        print("load im again")
        im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        print("flip im")
        im.close()
        print("close im")
    except: 
    #manage excetions here
        print("File load Failed")
        #we dont want straight to exit, not yet
        #sys.exit(0)

    f = imageio.imread(filename, as_gray=True)
    try:
        imageio.verify(f)
        print("try verify file")
    # do stuff
    except IOError:
    # filename not an image file
        print("file is no image")
        sys.exit(0)

    def img_estim(img, thrshld):
        is_light = np.mean(img) > thrshld
        print(np.mean(img))
        #return 'light' if is_light else os.remove(filename)
        if is_light == 0:
#            os.remove(filename)
             print("Delete this file")

    img_estim(f, 40)
    print(img_estim(f, 40))
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

