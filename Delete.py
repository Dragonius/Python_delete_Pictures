import sys
import os
import imageio
import numpy as np
#from PIL import Image
import image
import pytest
import pathlib

def ex():
    raise SystemExit(1)

def test_exits():
    with pytest.raises(SystemExit):
        ex()

files = [p for p in pathlib.Path('test_files').iterdir() if p.is_file()]


@pytest.fixture
def image(request):
    path = request.param
    with path.open('rb') as fileobj:
        yield fileobj.read()
    #141.12778

def main():
    filename = sys.argv[-1]

    try:
        im = Image.load(filename)
        im.verify() #Need to find defects
        im.close() #reload is needes to continue
        im = Image.load(filename)
        #im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        im.transpose(Image.FLIP_LEFT_RIGHT)
        im.close()
    except:    #If Error -> Exit program
        sys.exit(0)

    f = imageio.imread(filename, as_gray=True)
    try:
        imageio.verify(f) # Verify more
    except IOError:
        # ERROR -> filename not an image file
        sys.exit(0)

    def img_estim(img, thrshld):
        is_light = np.mean(img) > thrshld
        #print(np.mean(img))
        #return 'light' if is_light else os.remove(filename)
        if is_light == 0:
            os.remove(filename)

    img_estim(f, 40)
    #print(img_estim(f, 40)) # if black is more that 255/100*40 (i think)
    #print #new line

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt: #Ctrl-C Try stop program
        print('Interrupted')
        try: 
            sys.exit(0)
        except SystemExit:
            os._exit(0)
