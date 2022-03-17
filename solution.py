# coding:utf-8
# 具体解决方案实现
# 参考http://www.artificialworlds.net/presentations/tweetable-art/tweetable-art.html
# 及 https://codegolf.stackexchange.com/questions/35569/tweetable-mathematical-art


import math


"""
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
"""


"""
# 模板
def RD(i, j, DIM = 1024):
    
    return r


def GR(i, j, DIM = 1024):
    
    return g
    
    
def BL(i, j, DIM = 1024):
    
    return b
"""


"""
# 纯红色
def RD(i, j, DIM = 1024):
    r = 255
    return r


def GR(i, j, DIM = 1024):
    g = 0
    return g
    
    
def BL(i, j, DIM = 1024):
    b = 0
    return b
"""


"""
# 色阶
def RD(i, j, DIM = 1024):
    r = i
    return r


def GR(i, j, DIM = 1024):
    g = i
    return g
    
    
def BL(i, j, DIM = 1024):
    b = j
    return b
"""


"""
# 地板
def RD(i, j, DIM = 1024):
    s = 3.0/(j+99.0)
    r = (int((i+DIM)*s + j*s)%2 + int((DIM*2-i)*s + j*s)%2)*127
    return r


def GR(i, j, DIM = 1024):
    s = 3.0/(j+99.0)
    g = (int((i+DIM)*s + j*s)%2 + int((DIM*2-i)*s + j*s)%2)*127
    return g
    
    
def BL(i, j, DIM = 1024):
    s = 3.0/(j+99.0)
    b = (int((i+DIM)*s + j*s)%2 + int((DIM*2-i)*s + j*s)%2)*127
    return b
"""


"""
# 立体地板
def RD(i, j, DIM = 1024):
    s = 3.0/(j+99.0)
    y = (j+math.sin(i*i+(j-700)**2*5/100.0/DIM)*35)*s
    r = (int((i+DIM)*s + y)%2 + int((DIM*2-i)*s + y)%2)*127
    return r


def GR(i, j, DIM = 1024):
    s = 3.0/(j+99.0)
    y = (j+math.sin(i*i+(j-700)**2*5/100.0/DIM)*35)*s
    g = (int((i+DIM)*s + y)%2 + int((DIM*2-i)*s + y)%2)*127
    return g
    
    
def BL(i, j, DIM = 1024):
    s = 3.0/(j+99.0)
    y = (j+math.sin(i*i+(j-700)**2*5/100.0/DIM)*35)*s
    b = (int((i+DIM)*s + y)%2 + int((DIM*2-i)*s + y)%2)*127
    return b
"""


"""
# 有颜色的立体地板
def RD(i, j, DIM = 1024):
    s = 3.0/(j+99.0)
    y = (j+math.sin(i*i+(j-700)**2*5/100.0/DIM)*35)*s
    r = (int((i+DIM)*s + y)%2 + int((DIM*2-i)*s + y)%2)*127
    return r


def GR(i, j, DIM = 1024):
    s = 3.0/(j+99.0)
    y = (j+math.sin(i*i+(j-700)**2*5/100.0/DIM)*35)*s
    g = (int(5*(i+DIM)*s + y)%2 + int(5*(DIM*2-i)*s + y)%2)*127
    return g
    
    
def BL(i, j, DIM = 1024):
    s = 3.0/(j+99.0)
    y = (j+math.sin(i*i+(j-700)**2*5/100.0/DIM)*35)*s
    b = (int(29*(i+DIM)*s + y)%2 + int(29*(DIM*2-i)*s + y)%2)*127
    return b
"""


"""
# 分形
def RD(i, j, DIM = 1024):
    x = 0.0
    y = 0.0
    for k in range(256):
        a = x**2 - y**2 + (i - 768.0)/512
        y = 2*x*y + (j - 512.0)/512
        x = a
        if x**2+y**2 > 4:
            break
    if k > 31:
        r = 256
    else:
        r = k*8
    return r


def GR(i, j, DIM = 1024):
    x = 0.0
    y = 0.0
    for k in range(256):
        a = x**2 - y**2 + (i - 768.0)/512
        y = 2*x*y + (j - 512.0)/512
        x = a
        if x**2+y**2 > 4:
            break
    if k > 63:
        g = 256
    else:
        g = k*4
    return g
    
    
def BL(i, j, DIM = 1024):
    x = 0.0
    y = 0.0
    for k in range(256):
        a = x**2 - y**2 + (i - 768.0)/512
        y = 2*x*y + (j - 512.0)/512
        x = a
        if x**2+y**2 > 4:
            break
    b = k
    return b
"""


# """
# 另一个分形
def RD(i, j, DIM = 1024):
    x = 0.0
    y = 0.0
    for k in range(256):
        a = x**2 - y**2 + (i - 768.0)/512
        y = 2*x*y + (j - 512.0)/512
        x = a
        if x**2+y**2 > 4:
            break
    r = math.log(k)*47
    return r


def GR(i, j, DIM = 1024):
    x = 0.0
    y = 0.0
    for k in range(256):
        a = x**2 - y**2 + (i - 768.0)/512
        y = 2*x*y + (j - 512.0)/512
        x = a
        if x**2+y**2 > 4:
            break
    g = math.log(k)*47
    return g
    
    
def BL(i, j, DIM = 1024):
    x = 0.0
    y = 0.0
    for k in range(256):
        a = x**2 - y**2 + (i - 768.0)/512
        y = 2*x*y + (j - 512.0)/512
        x = a
        if x**2+y**2 > 4:
            break
    b = 128 - math.log(k)*23
    return b
# """