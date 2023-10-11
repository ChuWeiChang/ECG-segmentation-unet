# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 20:07:40 2021

@author: duked
"""
def peaks(signal):
    import numpy as np
    from scipy.signal import find_peaks
    import matplotlib.pyplot as plt
    h = 40
    x, _ = find_peaks(signal, height=h)
    while(len(x)<=5):
        print("ss:",len(x))
        h -=5
        x, _ = find_peaks(signal, height=h)
    print("ss1:",len(x))
    return len(x)
def to1D(img):
    img = cv2.flip(img, 0)
    y, x = img.shape
    arr=[0]
    next_ = 0
    for i in range(1,x):
        next_ = arr[i-1]
        for j in range(y):
            if img [j, i] == 0:
                next_ = j
        arr.append(next_)
    return arr     
#--------------------
import cv2
path = "./EKG/EKG_001-120/6.jpg" 

img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
x=[115, 1345]
y=[830, 890]
img[812:832,132:153] = 255
img = img[y[0]:y[1],x[0]:x[1]]
ret, img = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
signal = to1D(img)
peak = peaks(signal)
print("heart beats:", peak*6)