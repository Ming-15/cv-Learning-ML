import cv2
import numpy as np
import matplotlib as plt

path0 = r'C:\Users\dyrs-ai-win10\Desktop\forpractice\cv\test_pic'
file0 = path0 + r'\001.jpg'
word0 = path0 + r'\word_001.jpg'
word1 = cv2.imread(r'C:\Users\dyrs-ai-win10\Desktop\forpractice\cv\test_pic\5_2_17_44_10.jpg')
word = cv2.imread(word0)
img = cv2.imread(file0)
#日常gbr
''' # basic

print(img[100,100])
#单个像素，要操作最好别用遍历式

a = img.item(10,10,2)
print(a)
img.itemset((10,10,2),100)
print(img.item(10,10,2))
print(a)

print(img.shape,'行列数')
print(img.size, '像素数')
print(img.dtype, '元素类型,debug必备')

area = img[100:200, 150:250]
cv2.imshow('area', area)
'''

#cv2.imshow('bgr',img)
b, g, r = cv2.split(img)
# 警告：cv2.split() 是一个比较耗时的操作。只有真正需要时才用它，能用 Numpy 索引就尽量用
# cv2.imshow('b',b)
#蓝色通道亮度
# bl = img        #这是一个指针操作，bl和img 都指向了同一张图片
bl = img.copy()     #复制一个新的副本
bl[:,:,1:] = 0      #其他通道置零
# cv2.imshow('bl', bl)
#蓝色通道图像效果
'''
# cv2.imshow('g',g)
# cv2.imshow('r',r)
rgb = cv2.merge((r, g, b))
cv2.imshow('rgb',rgb)


#cv2.copyMakeBorder()        #扩边函数
x = np.uint8([250])
y = np.uint8([10])
print( cv2.add(x,y)) # 250+10 = 260 => 255 4 [[255]] 5
print( x+y ) # 250+10 = 260 % 256 = 4
'''
# add = cv2.addWeighted(bl,0.5,img,0.5,0)
# cv2.imshow('add', add)
#可以尝试利用调色板做一个滤镜了

#比例是3:2，先剪切图片
print(word.shape)
'''在缩放时我们推荐使用cv2.INTER_AREA， 在扩展时我们推荐使用 v2.INTER_CUBIC（慢) 和 v2.INTER_LINEAR。
 默认情况下所有改变图像尺寸大小的操作使用的插值方法都是cv2.INTER_LINEAR。
  你可以使用下面任意一种方法改变图像的尺寸：
  res=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
'''
w = cv2.resize(word, (1200,800), interpolation=cv2.INTER_CUBIC)        #参数中（x,y）,即1200列，800行
print(w.shape)

# cv2.imshow('word',w)
# cv2.imshow('ori', img)
# add = cv2.addWeighted(w,0.5,img,0.5,0)
# cv2.imshow('add', add)


ret, thresh1 = cv2.threshold(img, 1, 255, cv2.THRESH_BINARY)

ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
titles = ['img', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()



# rows,cols,channels = w.shape
# roi = img[0:rows, 0:cols ]
# imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(imggray, 175, 255, cv2.THRESH_BINARY)
# mask_inv = cv2.bitwise_not(mask)





cv2.waitKey(0)
