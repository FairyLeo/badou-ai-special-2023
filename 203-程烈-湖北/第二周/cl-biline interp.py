import cv2
import numpy as np

# 读取图片
img = cv2.imread('D:\\BaiduNetdiskDownload\\CV\\lenna.png')

# 获取图片的宽度和高度
height, width = img.shape[:2]

# 设置新的宽度和高度
new_width, new_height = int(width * 1.5), int(height * 1.5)

# 创建一个新的空白图片，大小为新的宽度和高度
new_img = np.zeros((new_height, new_width, 3), dtype=np.uint8)

# 计算缩放比例
scale_x, scale_y = width / new_width, height / new_height

# 对新图片的每个像素进行双线性插值
for i in range(new_height):
    for j in range(new_width):
        # 计算原图中对应的位置
        x, y = j * scale_x, i * scale_y

        # 计算周围的四个点的位置
        x1, y1 = int(x), int(y)
        x2, y2 = min(x1 + 1, width - 1), min(y1 + 1, height - 1)

        # 计算插值权重
        dx, dy = x - x1, y - y1

        # 对每个通道进行双线性插值
        for k in range(3):
            new_img[i, j, k] = (1 - dx) * (1 - dy) * img[y1, x1, k] + dx * (1 - dy) * img[y1, x2, k] + (1 - dx) * dy * img[y2, x1, k] + dx * dy * img[y2, x2, k]

# 显示原始图片和插值后的图片
cv2.imshow('Original Image', img)
cv2.imshow('Bilinear Interpolation', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
