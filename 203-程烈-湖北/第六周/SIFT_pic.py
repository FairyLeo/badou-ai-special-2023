import cv2
import numpy as np

# 读取两张图片
img1 = cv2.imread('1-1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('1-2.jpg', cv2.IMREAD_GRAYSCALE)

# 创建SIFT对象
sift = cv2.SIFT_create()

# 检测特征点和描述符
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# 使用BFMatcher匹配描述符
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

# 应用比率测试
good_matches = []
for m, n in matches:
    if m.distance < 0.5 * n.distance:
        good_matches.append(m)

# 绘制匹配结果
img_matches = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# 将相同的特征点用绿色圆圈标记，不同的特征点用红色圆圈标记
for match in good_matches:
    img1_idx = match.queryIdx
    img2_idx = match.trainIdx
    (x1, y1) = kp1[img1_idx].pt
    (x2, y2) = kp2[img2_idx].pt
    color = (0, 255, 0) if img1_idx == img2_idx else (0, 0, 255)
    cv2.circle(img_matches, (int(x1), int(y1)), 15, color, -1)
    cv2.circle(img_matches, (int(x2) + int(img1.shape[1]), int(y2)), 15, color, -1)
    #在img_matches图像上画一个圆。圆的中心坐标是(int(x1), int(y1))，半径是8，颜色是上面设置的color，-1表示这个圆的线宽是图像的宽度

# 设置窗口大小
cv2.namedWindow('Matches', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Matches', 3000, 2500)

# 显示标记后的图片
cv2.imshow('Matches', img_matches)
cv2.waitKey(0)
cv2.destroyAllWindows()
