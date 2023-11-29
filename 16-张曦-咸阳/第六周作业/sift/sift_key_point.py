import cv2
import numpy as np


def drawMatchKnn_cv2(img1_gray, kp1, img2_gray, kp2, goodMatch):
    h1, w1 = img1_gray.shape[:2]
    h2, w2 = img2_gray.shape[:2]
    combine_pic = np.zeros((max(h1, h2), w1 + w2, 3), np.uint8)

    combine_pic[:h1, :w1] = img1_gray
    combine_pic[:h2, w1:w1 + w2] = img2_gray

    p1 = [kpp.queryIdx for kpp in goodMatch]
    p2 = [kpp.trainIdx for kpp in goodMatch]

    post1 = np.int32([kp1[kpp1].pt for kpp1 in p1])
    post2 = np.int32([kp2[kpp2].pt for kpp2 in p2]) + (w1, 0)

    for (x1, y1), (x2, y2) in zip(post1, post2):
        cv2.line(combine_pic, (x1, y1), (x2, y2), (255, 0, 0))

    cv2.namedWindow("match", cv2.WINDOW_NORMAL)
    cv2.imshow("match", combine_pic)


img1_gray = cv2.imread("iphone1.pn")
img2_gray = cv2.imread("iphone2.png")

# sift = cv2.SIFT()
sift = cv2.xfeatures2d.SIFT_create()
# sift = cv2.SURF()

kp1, des1 = sift.detectAndCompute(img1_gray, None)
kp2, des2 = sift.detectAndCompute(img2_gray, None)

# BFmatcher with default parms bf.match对两个描述符集合进行暴力匹配
bf = cv2.BFMatcher(cv2.NORM_L2)

"""
可以查询数据集中每个描述符的 k 个最佳匹配项。
queryDescriptors：原图
trainDescriptors：搜索的图片
matches：匹配的结果
"""
matches = bf.knnMatch(des1, des2, k=2)
"""
返回的matches，部分元素如下：
distance：两个特征点的距离
imgIdx：训练图片的索引
queryIdx：query descriptor index 原图的描述符索引
trainIdx：train descriptor index 搜索图片的描述符索引
"""

goodMatch = []
for m, n in matches:
    if m.distance < 0.50 * n.distance:
        goodMatch.append(m)
        print("m.queryIdx={}, m.trainIdx={}".format(m.queryIdx, m.trainIdx))

drawMatchKnn_cv2(img1_gray, kp1, img2_gray, kp2, goodMatch[:16])

cv2.waitKey(0)
cv2.destroyAllWindows()
