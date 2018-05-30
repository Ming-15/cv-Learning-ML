# _*_ coding: utf-8 _*_
'''
Created on Sat April 27 00:00 2018
@ author ML Zhang
引用全局变量，不需要golbal声明，修改全局变量，需要使用global声明，
特别地，列表、字典等如果只是修改其中元素的值，可以直接使用全局变量，不需要global声明。
'''
import cv2
import numpy as np


'''
#mouse callback function
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:        #看清楚是左键双击
        cv2.circle(img, (x,y), 100, (255,255,255), -1)

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('111')
cv2.setMouseCallback('111',draw_circle)
while True :                            #被关闭也不断循环创建直到esc
    cv2.imshow('111',img)
    if cv2.waitKey(20)&0xff==27:        #按位与，输入建的ASCII码
        break
cv2.destroyAllWindows()
'''
'''鼠标定点之间画矩形方形
drawing = False
hold = False

mode = True     #mode 形状，可以改标签
ix, iy = -1, -1

#回调函数
def draw_circle(event, x, y, flags, param):
    global ix,iy,drawing,mode,hold
    if event== cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y
    elif event== cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        hold = True
        # if drawing:
        #     if mode:
        #         cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), 1)    #非填充，看出他是一个动态画，时间间隔读取鼠标数据
        #     else:
        #         r = int(np.sqrt((ix-x)**2 + (iy-y)**2))
        #         cv2.circle(img, (ix, iy), r, (0, 0, 255), -1)
        #         # cv2.circle(img, (x,y), r, (0,0,255), -1)      #圆心变了试试

    elif event == cv2.EVENT_LBUTTONUP :
        #松开鼠标才画，注释掉上一个动态绘画
        if drawing:
            if hold:
                if mode:
                    cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), 1)
                else:
                    r = int(np.sqrt((ix-x)**2 + (iy-y)**2))
                    cv2.circle(img, (ix, iy), r, (0, 0, 255), 1)
        drawing = False
        hold = False

        #松开，不在画

img = np.zeros((1024,1024,3), np.uint8)
cv2.namedWindow('15')
cv2.setMouseCallback('15',draw_circle)
while True:
    cv2.imshow('15', img)
    k = cv2.waitKey(1) & 0xff
    if k == ord('m') or k == ord('M'):
        mode = not mode
    elif k == 27 :
        break
'''

'''调色板'''
def nothing(x):
    pass

img = np.zeros((1024,1024,3),np.uint8)

cv2.namedWindow('trace')

cv2.createTrackbar('R','trace',0,255,nothing)
cv2.createTrackbar('G','trace',0,255,nothing)
cv2.createTrackbar('B','trace',0,255,nothing)

switch = '0:oFF\n1:ON'
cv2.createTrackbar(switch, 'trace', 0, 1, nothing)
while True:
    cv2.imshow('trace',img)
    k = cv2.waitKey(1)&0xFF         #时间设置为1毫秒，刚好让你感觉像没有停顿啥的
    if k == 27:
        break
    r = cv2.getTrackbarPos('R','trace')
    g = cv2.getTrackbarPos('G','trace')
    b = cv2.getTrackbarPos('B','trace')
    s = cv2.getTrackbarPos(switch,'trace')

    if s==0:
        img[:] = 0
    else:
        img[:][1] = [b,g,r]
    # print(b)
    print(img)
        #多重列表嵌套python 自己匹配了底层赋值的元素类型，这里相当于img[:][:]

cv2.destroyAllWindows()

