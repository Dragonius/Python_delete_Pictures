from multiprocessing import Process

import sys
import os
import imageio
import numpy as np
from PIL import Image

def main(file):
    print("start dealng files")
    filename = file
    print(filename)

    try:
        im = Image.open(filename)
        im.verify() #I perform also verify, don't know if he sees other types o defects
        im.close() #reload is necessary in my case
        #Obselect
        #im = Image.load(filename) 
        #im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        #im.close()
        #print("try 1 success")
    except: 
    #manage excetions here
        print("try 1 failed")
        sys.exit(0)

    #obselete
    #f = imageio.imread(filename, as_gray=True)
    try:
        f = imageio.imread(filename, mode='L')
        #print("Try 2 success")
    #obselete
    #try:
    #    imageio.verify(f)
    # do stuff
    except IOError:
    # filename not an image file
        print("IO error")
        sys.exit(0)

    def img_estim(img, thrshld):
        is_light = np.mean(img) > thrshld
        #print(np.mean(img))
        #return 'light' if is_light else os.remove(filename)
        if is_light == 0:
            os.remove(filename)

    img_estim(f, 40)
    #print(img_estim(f, 40))
    #print

if __name__ == '__main__':
    p = Process(target=main, args=(sys.argv[-1],))
    #print("start")
    p.start()
    #print("join process")
    p.join()
#    try:
#        main()
#    except KeyboardInterrupt:
#        print('Interrupted')
#        try:
#            sys.exit(0)
#        except SystemExit:
#            os._exit(0)

