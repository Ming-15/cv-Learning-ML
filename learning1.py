# _*_ coding: utf-8 _*_
'''cv 基本操作和练习'''
import numpy as np
import cv2

path0 = r'C:\Users\dyrs-ai-win10\Desktop\forpractice\cv\test_pic'
file0 = path0 + r'\001.jpg'

img = cv2.imread(file0,1) #0代表黑白，1代表彩色 或者参数
# img = cv2.imread(file0,cv2.IMREAD_GRAYSCALE) #灰色

# cv2.namedWindow('02')
cv2.namedWindow('02',cv2.WINDOW_AUTOSIZE)#自己调节大小

cv2.imshow('02',img)    # imshow 的名字用到窗户名字会使用那个窗户
#cv2.waitKey(1000) #时间毫秒,为零无限等待.可以用于检测特定按键
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    s_file = path0 + r'\save_001.jpg'
    cv2.imwrite(s_file, img)
# cv2.destroyAllWindows() #关闭窗口

mg = cv2.imread(file0,cv2.IMREAD_GRAYSCALE) #灰色
cv2.imshow('reverse', mg[::-1, ::-1])   #列表嵌套列表【 图片【第一行灰点亮度】【】【】】
                                        # 正常图片【     【行  【r，g，b】 】 】
                                        #   cv的图片 【b,g,r】
# k = np.flipud(mg)     #flipud 会翻转列表
k = np.flipud([np.flipud(x) for x in mg ])
cv2.imshow('k', k)

from matplotlib import pyplot as plt

#CV用的是bgr顺序，mlp是RGB，需要调换顺序
# b,g,r = cv2.split(img)
# img2 = cv2.merge([r,g,b])
img2 = img[:, :, ::-1]      #顺序是相反的，反着读取就行了,对嵌套的第三层列表进行反着读
plt.imshow(img2,cmap='gray',interpolation='bicubic')
plt.xticks([]),plt.yticks([])   # to hide tick values on x and y axis
plt.show()


# # _*_ coding: utf-8 _*_
# '''视频'''
# import numpy as np
# import cv2
#
# cap = cv2.VideoCapture(0)

import numpy as np
import cv2
import matplotlib as mlp
# create s black image
img = np.zeros((512,512,3), np.uint8)

'''所有的绘图函数的返回值都是 None，所以不能使用 img = cv2.line(img,(0,0),(511,511),(255,0,0),5)。
'''

#draw a diagonal blue line with thickness of 5 px
cv2.line(img, (0,0), (511,511), (255,0,0), 10)

cv2.circle(img, (447,63), 63, (0,255,0), 1)     #-1 填充形状

cv2.ellipse(img, (250,250), (100,50), 0, 0, 180, (255,255,0), 1)


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'ohhhhhh', (10,500), font, 4, (255,255,255), 100) #位置，大小，颜色，，字粗细

cv2.imshow('01', img)
# cv2.imshow('01', img[::-1]) #上下行调换

#画多边形，略

cv2.waitKey(0)
cv2.destroyAllWindows()

event = [i for i in dir(cv2) if 'EVENT' in i]
print(event)
#所有鼠标操作


