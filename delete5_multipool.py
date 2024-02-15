import multiprocessing
import sys
import os
import numpy as np
from PIL import Image
if sys.version_info < (3, 7):
    import imageio
else:
    import imageio.v2 as imageio


def process(pathfilename):
    #pass # do stuff to a file
    f = imageio.imread(pathfilename, mode='L')
    is_light = np.mean(f) > 40
    #Print lightness value
    #print(np.mean(f))
    #alternative way to do, when calling returns
    #return 'light' if is_light else os.remove(filename)
    if is_light == 0:
        #print if file will be deleted
        #print("test DELETE ", pathfilename)
        os.remove(pathfilename)
    #if is_light == 1:
        #print if file is keep
        #print("test KEEP ", pathfilename)



def main():
    """Start main program."""
    path = sys.argv[-1]
    #show argv data and lenght
    #print(sys.argv, len(sys.argv))
    #kill ifnot arguments.
    if len(sys.argv)<2:
        os._exit(0)

    dir_list = os.listdir(path)
    #sort file list, as dir_list cant be a mess order
    dir_list.sort()


    p = multiprocessing.Pool()
    for filename in os.listdir(path):
        if filename.endswith(".jpg"):
            pathfilename = path + filename
        #print(pathfilename)
        try:
            #Test files that can they be opended
            img = Image.open(pathfilename)
            #Perform also verify, don't know if he sees other types o defects
            img.verify()
            #close file
            img.close()
        except:
            print("Couldtn't open image file: ", pathfilename)


        # launch a process for each file (ish), using async ending.
        # The result will be approximately one process per CPU core available.
        p.apply_async(process, [pathfilename]) 

    p.close()
    p.join() # Wait for all child processes to close.


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
