# _*_ coding:utf-8 _*_
'''
choose your pen and draw a picture
created on 14:07 4/28/2018
@author ML Zhang
'''

import numpy as np
import cv2
import time

drawing = False
ix, iy = 0, 0

def nothing(x):
    pass

def draw(event,x,y,flags,param):
    global ix, iy, drawing
    if event== cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing :
            cv2.line(pic_win,(ix,iy), (x,y), (b,g,r),size)
            ix, iy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing =False

def change_pen(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONUP:
        return 1
def start(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONUP:
        return 1

def extend_picture():
    pass

pic_win = np.zeros((1024,1024,3), np.uint8)     #windows for picture
pic_win[:] = 255
pen_win = np.zeros((250,250,3), np.uint8)       #windows for choosing a pen

cv2.namedWindow('pen')
cv2.namedWindow('draw picture')

cv2.createTrackbar('R', 'pen', 0, 255, nothing)
cv2.createTrackbar('G', 'pen', 0, 255, nothing)
cv2.createTrackbar('B', 'pen', 0, 255, nothing)
cv2.createTrackbar('size','pen', 0, 100, nothing)

while True:
    cv2.imshow('pen', pen_win)
    r = cv2.getTrackbarPos('R', 'pen')
    g = cv2.getTrackbarPos('G', 'pen')
    b = cv2.getTrackbarPos('B', 'pen')
    size = cv2.getTrackbarPos('size', 'pen')

    pen_win[:] = [b,g,r]
    cv2.imshow('pen', pen_win)
    #显示当前笔的颜色

    cv2.imshow('draw picture', pic_win)

    cv2.setMouseCallback('draw picture',draw)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    if k == ord('s'):
        ti = time.localtime(time.time())
        tt = str(ti.tm_mon) + '_'+ str(ti.tm_mday) +'_'+ str(ti.tm_hour) +'_'\
             + str(ti.tm_min) +'_'+str(ti.tm_sec)
        path0 = r'C:\Users\dyrs-ai-win10\Desktop\forpractice\cv\test_pic'
        file0 = path0 +'\\'+ tt + '.jpg'

        cv2.imwrite(file0,pic_win)