#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/12/22 22:07
# @Author  : dly
# @File    : 01.py
# @Desc    :

import cv2 as cv
import numpy as np

base_dir = 'C:/Users/Dooooooooo21/Desktop/103D7000/'


# 属性
def values():
    img = cv.imread(base_dir + '_DSC6981.JPG', 1)
    print(img.shape)
    print(img.size)
    print(img.dtype)


# 拆分和合并图像通道
def split_and_merge(img):
    # split 耗时间
    b, g, r = cv.split(img)

    img = cv.merge((b, g, r))


# 图像融合
def img_merge():
    img1 = cv.imread(base_dir + '_DSC6981.JPG', 1)
    # 修改大小
    img1 = cv.resize(img1, (1200, 900), interpolation=cv.INTER_CUBIC)
    img2 = cv.imread(base_dir + '_DSC6884.JPG', 1)
    img2 = cv.resize(img2, (1200, 900), interpolation=cv.INTER_CUBIC)
    # 融合
    dst = cv.addWeighted(img1, 0.7, img2, 0.3, 0)
    cv.imshow('dst', dst)
    cv.waitKey(0)
    cv.destroyAllWindows()


img_merge()
