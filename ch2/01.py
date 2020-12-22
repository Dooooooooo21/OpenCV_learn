#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/12/22 21:31
# @Author  : dly
# @File    : 01.py
# @Desc    :

import cv2 as cv
import numpy as np

base_dir = 'C:/Users/Dooooooooo21/Desktop/103D7000/'


# 图像展示
def show():
    img = cv.imread(base_dir + '_DSC6981.JPG', 1)
    cv.imshow('image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


# 画线
def draw():
    # 创建黑色的图像
    img = np.zeros((512, 512, 3), np.uint8)
    # 绘制一条厚度为5的蓝色对角线
    cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
    cv.imshow('image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


draw()
