# coding:utf-8
# 画图程序的python移植
# 原版地址:https://codegolf.stackexchange.com/questions/35569/tweetable-mathematical-art


import matplotlib.pyplot as plt
import math
from PIL import Image
import numpy as np
import random


def GR(i, j):
    # return math.cos(math.atan2(j-512,i-512)/2-2*math.acos(-1)/3)*255
    return random.randint(0, 256)
    
    
def BL(i, j):
    # return math.cos(math.atan2(j-512,i-512)/2+2*math.acos(-1)/3)*255
    return random.randint(0, 256)
    
    
def RD(i, j):
    # return math.cos(math.atan2(j-512,i-512)/2)*255
    return random.randint(0, 256)


# 画图程序，在指定坐标处画点
def pixel_write(data, filename = "result.jpg"):
    data = np.array(data)
    data = np.asarray(data, np.uint8)
    # print(data)
    pic = Image.fromarray(data)
    pic.save(filename)
    
    
# 主程序
def main():
    DIM = 1024
    plt.figure()
    data = []
    for i in range(DIM):
        row = []
        for j in range(DIM):
            print(i, j)
            r = RD(i, j)%255
            g = GR(i, j)%255
            b = BL(i, j)%255
            c = (r, g, b)
            # print(c)
            row.append(c)
        data.append(row)
        # del(row)
    pixel_write(data)
    plt.close()


if __name__ == "__main__":
    main()