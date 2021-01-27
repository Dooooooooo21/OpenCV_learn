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


# 性能
def tick_count():
    # 检查是否启用了优化
    print(cv.useOptimized())

    # 关闭优化
    cv.setUseOptimized(False)

    e1 = cv.getTickCount()
    # 执行代码
    e2 = cv.getTickCount()
    time = (e2 - e1) / cv.getTickFrequency()


# tick_count()

def nothing(x):
    pass


# 滑动条，调色板
def trackBar():
    img = np.zeros((512, 512, 3), np.uint8)
    cv.namedWindow('image')

    cv.createTrackbar('R', 'image', 0, 255, nothing)
    cv.createTrackbar('G', 'image', 0, 255, nothing)
    cv.createTrackbar('B', 'image', 0, 255, nothing)

    switch = '0:OFF\n1:ON'
    cv.createTrackbar(switch, 'image', 0, 1, nothing)

    while 1:
        cv.imshow('image', img)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break

        r = cv.getTrackbarPos('R', 'image')
        g = cv.getTrackbarPos('G', 'image')
        b = cv.getTrackbarPos('B', 'image')
        s = cv.getTrackbarPos(switch, 'image')

        if s == 0:
            img[:] = 0
        else:
            img[:] = [b, g, r]

    cv.destroyAllWindows()


trackBar()
