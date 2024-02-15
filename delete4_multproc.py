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
        im = Image.load(filename)
        im.verify() #I perform also verify, don't know if he sees other types o defects
        im.close() #reload is necessary in my case
        im = Image.load(filename) 
        im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        im.close()
    except: 
    #manage excetions here
        sys.exit(0)

    #obselete
    #f = imageio.imread(filename, as_gray=True)
    f = imageio.imread(filename, mode='L')
    try:
        imageio.verify(f)
        print("verify 1")
    # do stuff
    except IOError:
    # filename not an image file
        print("IO error")
        sys.exit(0)

    def img_estim(img, thrshld):
        is_light = np.mean(img) > thrshld
        print(np.mean(img))
        #return 'light' if is_light else os.remove(filename)
        if is_light == 0:
            os.remove(filename)

    img_estim(f, 40)
    #print(img_estim(f, 40))
    #print

if __name__ == '__main__':
    p = Process(target=main, args=('sys.argv[-1]',))
    print("start")
    p.start()
    print("join process")
    p.join()
#    try:
#        main()
#    except KeyboardInterrupt:
#        print('Interrupted')
#        try:
#            sys.exit(0)
#        except SystemExit:
#            os._exit(0)

