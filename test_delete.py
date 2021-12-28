#!/usr/bin/env python3

import sys
import os
import imageio
import numpy as np

#missing all comments
def main():
    filename = "./test_files/Clouds_test.jpg"

    f = imageio.imread(filename, as_gray=True)

    def img_estim(img, thrshld):
        is_light = np.mean(img) > thrshld
        print(np.mean(img))
        print(is_light)
        #return 'light' if is_light else os.remove(filename)
        if is_light == 0:
#               os.remove(filename)
            print("delete this file")
        
    img_estim(f, 40)
    #print(img_estim(f, 40))
    #print

def test_imgislight():
#    imagetreshold = 141.1277
    filename = "./test_files/Clouds_test.jpg"
    f = imageio.imread(filename, as_gray=True)
    is_light = np.mean(f) > 40
    print(is_light)
    assert is_light == True
    

def test_imagetresholdvalue():
     imagetresholdbig = 141.12780
     imagetresholdsmall = 141.12770
     filename = "./test_files/Clouds_test.jpg"
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
