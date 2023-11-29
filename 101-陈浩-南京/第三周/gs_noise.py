import numpy as np
import cv2
from numpy import  shape
import random

def GaussianNoise(src,means,sigma,percentage):
    NoiseImg = src
    NoiseNum = int(percentage * src.shape[0] * src.shape[1])
    for i in range(NoiseNum):
        #循环取点，在x和y值上随机添加值
        randX = random.randint(0,src.shape[0] - 1)
        randY = random.randint(0,src.shape[1] - 1)

        #在原有的灰度值上添加随机数
        NoiseImg[randX,randY] = NoiseImg[randX,randY] + random.gauss(means,sigma)
        if NoiseImg[randX,randY] < 0:
            NoiseImg[randX, randY] = 0
        elif NoiseImg[randX,randY] > 255:
            NoiseImg[randX, randY] = 255
    return NoiseImg

img = cv2.imread('lenna.png',0)
img1 = GaussianNoise(img,2,4,0.8)
img = cv2.imread('lenna.png')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('source',img2)

# cv2.imwrite('lenann_noise2.png',img1)
cv2.imshow('lenna_GaussianNoise',img1)
cv2.waitKey(0)