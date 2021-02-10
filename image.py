import sys
import os
import imageio
import numpy as np

def main():
    filename = sys.argv[-1]


    f = imageio.imread(filename, as_gray=True)

    def img_estim(img, thrshld):
        is_light = np.mean(img) > thrshld
        print(np.mean(img))
        return 'light' if is_light else 'dark'

    print(img_estim(f, 40))
    print

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
