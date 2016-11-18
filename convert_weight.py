import sys
import numpy as np
from PIL import Image

Byte_size = 8
Addr_size = 100
Wide_size = 4
Raw_size = 2

def hex2int(byte_data):
    byte_data_ord = []
    byte_addr = []

    for i in xrange(Byte_size * Addr_size):
        byte_data_ord.append(ord(byte_data[i]))
        byte_data_ord[i] = byte_data_ord[i] << (i % 8) * 8

    for i in xrange(Byte_size * Addr_size):
        if i % 8 == 0:
            tmp = byte_data_ord[i]
            for bit in xrange(Byte_size):
                tmp = tmp | byte_data_ord[i+bit]
            byte_addr.append(tmp)
        else:
            continue

    return byte_addr


def create_bw(data_arr):
    bitmap = []
    for bit in xrange((Byte_size / 2) * Wide_size):
        if (data_arr >> bit) & 1 == 1:
            # black(0)
            color = 0
        else:
            # white(255)
            color = 255
        for i in xrange(bit):
            bitmap.append([color, color, color])
    return bitmap


if __name__ == '__main__':
    argvs = sys.argv

    # ideal : only consists of a_0 ~ a_99 
    f_ideal = open('result_ideal', "rb")
    ideal_data = f_ideal.read()
    ideal_addr = []    
    ideal_addr = hex2int(ideal_data)

    # calculate the average of ideal_addr
    ideal_addr_np = np.array(ideal_addr)
    ave = int(np.average(ideal_addr_np))
    # print('average', ave)

    f = open(argvs[1], "rb")
    data = f.read()
    addr = []
    diff = []
    addr = hex2int(data)
    
    for i in xrange(Addr_size):
        diff.append(abs(addr[i] - ave))

    bw_arr = []

    for x in diff:
        bw_arr.append(create_bw(x))

    # for i in xrange(Addr_size):
    #     print(hex(diff[i]))
    #     print(bw_arr[i])
            

    ip = Image.fromarray(np.uint8(np.array(bw_arr)))
    ip.save('input0.bmp')

