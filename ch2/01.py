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


# 读取摄像头/视频
def video_cap():
    vc = cv.VideoCapture(0)
    if vc.isOpened():
        open, frame = vc.read()
    else:
        open = False

    while open:
        ret, frame = vc.read()
        if frame is None:
            break
        if ret:
            pass


# 画
def draw():
    # 创建黑色的图像
    img = np.zeros((512, 512, 3), np.uint8)

    # 绘制一条厚度为5的蓝色对角线
    cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

    # 图像的右上角绘制一个绿色矩形
    cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

    # 在上面绘制的矩形内绘制一个圆
    cv.circle(img, (447, 63), 63, (0, 0, 255), -1)

    # 在白色图像上写入OpenCV
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv.LINE_AA)

    cv.imshow('image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def event_list():
    events = [i for i in dir(cv) if 'EVENT' in i]
    # 事件
    print(events)


def mouse_draw():
    # 鼠标回调函数
    def draw_circle(event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDBLCLK:
            cv.circle(img, (x, y), 100, (255, 0, 0), -1)

    # 创建一个黑色的图像，一个窗口，并绑定到窗口的功能
    img = np.zeros((512, 512, 3), np.uint8)
    cv.namedWindow('image')
    cv.setMouseCallback('image', draw_circle)
    while (1):
        cv.imshow('image', img)
        # 27 esc
        if cv.waitKey(20) & 0xFF == 27:
            break
    cv.destroyAllWindows()


mouse_draw()
