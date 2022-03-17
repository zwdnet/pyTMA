# coding:utf-8
# 画图程序的python移植
# 原版地址:https://codegolf.stackexchange.com/questions/35569/tweetable-mathematical-art


import matplotlib.pyplot as plt
import math
from PIL import Image
import numpy as np
import random
from solution import *
from tqdm import tqdm


# 画图程序，在指定坐标处画点
def pixel_write(data, filename = "result.jpg"):
    data = np.array(data)
    data = np.asarray(data, np.uint8)
    # print(data)
    pic = Image.fromarray(data)
    pic.save(filename)
    
    
# 主程序
def main(filename = "result.jpg"):
    DIM = 1024
    plt.figure()
    data = []
    print("正在绘图")
    for i in tqdm(range(DIM)):
        row = []
        for j in range(DIM):
            # print(i, j)
            r = RD(i, j, DIM = DIM)%256
            g = GR(i, j, DIM = DIM)%256
            b = BL(i, j, DIM = DIM)%256
            c = (r, g, b)
            # print(c)
            row.append(c)
        data.append(row)
        # del(row)
    pixel_write(data, filename = filename)
    plt.close()
    print("绘图完成")


if __name__ == "__main__":
    main(filename = "ans8.jpg")