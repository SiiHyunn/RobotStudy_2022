import cv2
import numpy as np

def mouse_callback(event, x, y, flags, param):
    if event == 1:
        print('B: ', param[y][x][0], '\nG: ', param[y][x][1], '\nR: ', param[y][x][2])
        print('=================================')

Path = 'Data/'
Name = 'lenna.tif'
src = Path + Name

#로버츠, 프리윗, 소벨은 에지 검출이기 때문에 grayscale로 불러와줌
color_img = cv2.imread(src)
img = cv2.imread(src, cv2.IMREAD_GRAYSCALE)

#필터값
roberts_x = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 0]])
roberts_y = np.array([[0, 0, -1], [0, 1, 0], [0, 0, 0]])

prewitt_x = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
prewitt_y = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])

sobel_x = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
sobel_y = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])

#공식에 맞게 계산&&정수화
roberts_x = cv2.convertScaleAbs(cv2.filter2D(img, -1, roberts_x))
roberts_y = cv2.convertScaleAbs(cv2.filter2D(img, -1, roberts_y))

prewitt_x = cv2.convertScaleAbs(cv2.filter2D(img, -1, prewitt_x))
prewitt_y = cv2.convertScaleAbs(cv2.filter2D(img, -1, prewitt_y))

sobel_x = cv2.convertScaleAbs(cv2.filter2D(img, -1, sobel_x))
sobel_y = cv2.convertScaleAbs(cv2.filter2D(img, -1, sobel_y))

#x와 y값을 하나로 합쳐줌
prewitt = cv2.addWeighted(prewitt_x, 1, prewitt_y, 1, 0)
roberts = cv2.addWeighted(roberts_x, 1, roberts_y, 1, 0)
sobel = cv2.addWeighted(sobel_x, 1, sobel_y, 1, 0)

#이미지 저장
cv2.imwrite('./Data/prewitt.png',prewitt)
cv2.imwrite('./Data/roberts.png',roberts)
cv2.imwrite('./Data/sobel.png',sobel)

#imshow
cv2.imshow('original', img)
cv2.imshow('prewitt', prewitt)
cv2.imshow('roberts', roberts)
cv2.imshow('sobel', sobel)

while cv2.waitKey(33) <= 0:
    cv2.setMouseCallback('img', mouse_callback, img)