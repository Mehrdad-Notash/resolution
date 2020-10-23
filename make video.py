#!/usr/bin/env python
# coding: utf-8

import cv2
import numpy as np
import glob
from resolution import *
def make_video(folder,out):
    img_array = []
    folder = glob.glob(folder)
    for file in folder:
        img = cv2.imread(file)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
    out = cv2.VideoWriter(out+'.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()


#image_shape = (512,512,3)
#g_model = define_generator(image_shape)
#model = g_model
#model.load_weights('model3.h5')   ###23760

#make_video('recon')




