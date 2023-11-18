import cv2
import numpy as np

# 读取图片
image = cv2.imread('_MG_8178.jpg', cv2.IMREAD_GRAYSCALE)

# 高斯滤波
gaussian_blur = cv2.GaussianBlur(image, (3, 3), 0.5)

# 计算梯度幅值和方向
gradient_x = cv2.Sobel(gaussian_blur, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(gaussian_blur, cv2.CV_64F, 0, 1, ksize=3)
gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
gradient_direction = np.arctan2(gradient_y, gradient_x) * 180 / np.pi

# 非极大值抑制
nms = np.zeros_like(gradient_magnitude)
for i in range(1, gradient_magnitude.shape[0] - 1):
    for j in range(1, gradient_magnitude.shape[1] - 1):
        direction = gradient_direction[i, j]
        if (0 <= direction < 45) or (157.5 <= direction <= 180):
            if (gradient_magnitude[i, j] >= gradient_magnitude[i, j - 1]) and (gradient_magnitude[i, j] >= gradient_magnitude[i, j + 1]):
                nms[i, j] = gradient_magnitude[i, j]
        elif (45 <= direction < 115):
            if (gradient_magnitude[i, j] >= gradient_magnitude[i - 1, j + 1]) and (gradient_magnitude[i, j] >= gradient_magnitude[i + 1, j - 1]):
                nms[i, j] = gradient_magnitude[i, j]
        elif (115 <= direction < 175):
            if (gradient_magnitude[i, j] >= gradient_magnitude[i - 1, j]) and (gradient_magnitude[i, j] >= gradient_magnitude[i + 1, j]):
                nms[i, j] = gradient_magnitude[i, j]
        else:
            if (gradient_magnitude[i, j] >= gradient_magnitude[i - 1, j - 1]) and (gradient_magnitude[i, j] >= gradient_magnitude[i + 1, j + 1]):
                nms[i, j] = gradient_magnitude[i, j]

# 双阈值算法检测和连接边缘
low_threshold = np.percentile(nms, 20)
high_threshold = np.percentile(nms, 80)
edges = np.zeros_like(nms)
strong_pixels = np.where((nms >= high_threshold) & (nms <= low_threshold))
weak_pixels = np.where((nms <= high_threshold) & (nms >= low_threshold))
edges[strong_pixels] = 255
edges[weak_pixels] = nms[weak_pixels]

# 输出结果
cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Canny Edge Detection', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Original Image', image.shape[1], image.shape[0])
cv2.resizeWindow('Canny Edge Detection', edges.shape[1], edges.shape[0])
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()