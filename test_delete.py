#!/usr/bin/env python3

import sys
import os
#import imageio
#Bellow import is getting ready to imageio V2 import when imageio v3 released
#import imageio.v2 as imageio
if sys.version_info < (3, 7):
    import imageio
else:
    import imageio.v2 as imageio
import numpy as np

#missing all comments
def main():
    #filename = "./test_files/Clouds_test.jpg"
    filename =  sys.argv[-1]
    #Bellow code is ImageIO Version 2
    f = imageio.imread(filename, mode='F')
    #bellow code is reading to imageio Version 3
    #f = iio.v3.imread(filename, as_gray=True)
    def img_estim(img, thrshld):
        is_light = np.mean(img) > thrshld
        print(np.mean(img))
        print(is_light)
        #return 'light' if is_light else os.remove(filename)
        if is_light == 0:
            #os.remove(filename)
            print("delete this file")
        
    img_estim(f, 40)
    #print(img_estim(f, 40))
    #print

def test_imgislight_TRUE():
    #imagetreshold = 141.1277
    filename = "./test_files/Clouds_test.jpg"
    f = imageio.imread(filename, mode=F)
    is_light = np.mean(f) > 40
    print(is_light)
    assert is_light == True
    

def test_imagetresholdvalue_TRUE():
    imagetresholdbig = 141.13
    imagetresholdsmall = 141.11
    filename = "./test_files/Clouds_test.jpg"
    f = imageio.imread(filename, mode=F)
    meanvalue1 = np.mean(f)
    meanvalue = round(meanvalue1,5)
    assert imagetresholdbig  >=  meanvalue >= imagetresholdsmall

def test_imgislight_FALSE():
    #imagetreshold = 141.1277
    filename = "./test_files/Clouds_test2.jpg"
    f = imageio.imread(filename, mode=F)
    is_light = np.mean(f) > 40
    print(is_light)
    assert is_light == False


def test_imagetresholdvalue_FALSE():
    imagetresholdbig = 39.99
    imagetresholdsmall = 1.00
    filename = "./test_files/Clouds_test2.jpg"
    f = imageio.imread(filename, mode=F)
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
