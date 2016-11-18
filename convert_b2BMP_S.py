import sys
from PIL import Image
import numpy as np


def create_wide(data_arr):
    ret_arr = []
    for data in data_arr:    
        for i in xrange(8):
            if (ord(data) >> i) & 1 == 1:
                color = 0
            else:
                color = 255
            ret_arr.append([color, color, color])
    return ret_arr

if __name__ == '__main__':
    argvs = sys.argv
    f = open(argvs[1], "rb")
    data = f.read()
    image_arr = []

    byte_arr = []
    for x in data:
        if len(byte_arr) < 16:
            byte_arr.append(x)
        else:
            image_arr.append(create_wide(byte_arr))
            byte_arr = [x]

    IA = Image.fromarray(np.uint8(np.array(image_arr)))
    # IA.save('input2.bmp')
    IA.save(argvs[2])
