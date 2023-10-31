import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray



#灰度
img = cv2.imread("lenna.png")
# h,w = img.shape[:2]
# img_gray = np.zeros([h,w],img.dtype)
# for i in range(h):
#     for j in range(w):
#         m = img[i,j]
#         img_gray[i,j] = int(m[0] * 0.11 + m[1]*0.59 + m[2]*0.3)


plt.subplot(221)
img = plt.imread("lenna.png")
# img = cv2.imread("lenna.png", False)
plt.imshow(img)
print("---image lenna----")
print(img)

img_gray = rgb2gray(img)
plt.subplot(222)
plt.imshow(img_gray,cmap='gray')

#二值化
# rows,cols = img_gray.shape
# for i in range(rows):
#     for j in range(cols):
#         if(img_gray[i,j] <= 0.5):
#             img_gray[i,j] = 0
#         else:
#             img_gray[i,j] = 1
# cv2.imshow("show gray",img_gray)
# cv2.waitKey()

img_binary = np.where(img_gray >= 0.5,1,0)
plt.subplot(223)
plt.imshow(img_binary,cmap='gray')
plt.show()










