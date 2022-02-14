# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

# def mouse_callback(event, x, y, flags, param):
#     if event == 1:
#         print('B: ', param[y][x][0], '\nG: ', param[y][x][1], '\nR: ', param[y][x][2])
#         print('=================================')

Path = './Data/'
Name = 'rabong2.jpg'
FullName = Path + Name

#이미지 읽기
img = cv.imread(FullName, 1)

#라인 그리기
cv.line(img, (0,256), (512,256), (255,0,0),2)
cv.line(img, (256,0), (256,512), (255,0,0),2)

xpos=[]
ypos=[]

for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        #오렌지색
        if 0<=img[x][y][0]<=100 and 70<=img[x][y][1]<=200 and 150<=img[x][y][2]<=255:
            img[x][y]=(0,0,255)
            xpos.append(x)
            ypos.append(y)

xpos=int(sum(xpos)/len(xpos))
ypos=int(sum(ypos)/len(ypos))

if 256<=xpos<512 and 0<=ypos<256:
    p=1
if 0<=xpos<256 and 0<=ypos<256:
    p=2
if 0<=xpos<256 and 256<=ypos<512:
    p=3
if 256<=xpos<512 and 256<=ypos<512:
    p=4

print("위치:",p,"사분면")
print("크기:",img.shape)

#이미지 출력하기
cv.imshow('result', img)
cv.waitKey()