# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 22:54:04 2021

@author: duked
"""
def split_12(img):
    import numpy as np
    new_img =[]
    x=(110,420,730,1040,1350)
    y = (370, 510, 650, 790)
    counter = 0
    for i in range(3):
        for j in range(4):
            #new_img = np.append(new_img, img[y[i]:y[i+1]-1,x[j]:x[j+1]-1,:])
            new_img.append(img[y[i]:y[i+1],x[j]:x[j+1],:])
            counter+=1
    new_img = np.array(new_img)
    np.reshape(new_img,(12,140,310,3))
    return new_img
#--------------------------------------------
import cv2
import os
path = "./EKG" #資料夾目錄
files= os.listdir(path) #得到資料夾下的所有檔名稱
for root, dirs, files in os.walk(path):
    for file in files:
        fullpath = os.path.join(root, file)
        img = cv2.imread(fullpath)
        new_img = split_12(img)
        for i in range(12):
             cv2.imshow(fullpath, new_img[i])
             cv2.waitKey(0)
