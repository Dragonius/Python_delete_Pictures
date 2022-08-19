#!/usr/bin/env python3

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
#print(dir_list)
#ask for arguments for directory, ifn't given any , exit

def main():
    path = sys.argv[-1]
    path = "./test_files/"
    if (path==""):
        os._exit(0)

    dir_list = os.listdir(path)
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
        #manage excetions here
            print("Couldtn't open image file ", pathfilename , " on img ")
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
                print("Delete this file")
                #os.remove(pathfilename)

        img_estim(f, 40)
        #print(img_estim(f, 40))
        #print
def test_imgislight_TRUE():
#    imagetreshold = 141.1277
    filename = path + dir_list[1]
    f = imageio.imread(filename, as_gray=True)
    is_light = np.mean(f) > 40
    print(is_light)
    assert is_light == True
    

def test_imagetresholdvalue_TRUE():
     imagetresholdbig = 141.13
     imagetresholdsmall = 141.11
     filename = "./test_files/Clouds_test.jpg"
     f = imageio.imread(filename, as_gray=True)
     meanvalue1 = np.mean(f)
     meanvalue = round(meanvalue1,5)
     assert imagetresholdbig  >=  meanvalue >= imagetresholdsmall

def test_imgislight_FALSE():
#   imagetreshold = 141.1277
    filename = "./test_files/Clouds_test2.jpg"
    f = imageio.imread(filename, as_gray=True)
    is_light = np.mean(f) > 40
    print(is_light)
    assert is_light == False


def test_imagetresholdvalue_FALSE():
     imagetresholdbig = 39.99
     imagetresholdsmall = 1.00
     filename = "./test_files/Clouds_test2.jpg"
     f = imageio.imread(filename, as_gray=True)
     meanvalue1 = np.mean(f)
     meanvalue = round(meanvalue1,5)
     assert imagetresholdbig  >=  meanvalue >= imagetresholdsmall

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
