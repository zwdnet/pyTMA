# coding:utf-8
# 具体解决方案实现


def RD(i, j, DIM = 1024):
    s = 3.0/(j+99.0)
    r = (int((i+DIM)*s+j*s)%2 + int((DIM*2-i)*s+j*s)%2)*127
    # print(r, type(r), r%255)
    return r


def GR(i, j, DIM = 1024):
    s = 3.0/(j+99.0)
    r = (int((i+DIM)*s+j*s)%2 + int((DIM*2-i)*s+j*s)%2)*127
    # print(r, type(r), r%255)
    return r
    
    
def BL(i, j, DIM = 1024):
    s = 3.0/(j+99.0)
    r = (int((i+DIM)*s+j*s)%2 + int((DIM*2-i)*s+j*s)%2)*127
    # print(r, type(r), r%255)
    return r