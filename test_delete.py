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
        #return 'light' if is_light else os.remove(filename)
        if is_light == 0:
#               os.remove(filename)
            print("delete this file")
        
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
