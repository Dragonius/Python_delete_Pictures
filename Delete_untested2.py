import sys
import os
import imageio
import numpy as np
from PIL import Image

def main():
    filename = sys.argv[-1]

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

    f = imageio.imread(filename, as_gray=True)
    try:
        imageio.verify(f)
    # do stuff
    except IOError:
    # filename not an image file
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
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

