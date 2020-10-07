import sys
import os
import imageio
import numpy as np

filename = sys.argv[-1]

f = imageio.imread(filename, as_gray=True)



def img_estim(img, thrshld):
    is_light = np.mean(img) > thrshld
    #print(np.mean(img))
    #return 'light' if is_light else os.remove(filename)
    if is_light == 0:
            os.remove(filename)

img_estim(f, 40)
#print(img_estim(f, 40))
#print
