import numpy as np
import cv2
from matplotlib import pyplot as plt

# 读取图像
image_path = "D:\\BaiduNetdiskDownload\\CV\\lenna.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# 获取图像宽高,不包含通道数,使用 image.shape[2]获取宽高和通道数
width, height = image.shape[:2]

# 最临近插值函数
def nearest_neighbor_interpolation(image, new_width, new_height):
    # 获取图像的像素值数组
    pixels = image
    # pixels = image.reshape(-1, 1)

    # 构建新的像素网格
    new_pixels = np.zeros((new_height, new_width), dtype=np.uint8)
    for i in range(new_height):
        for j in range(new_width):
            # 计算原始图像中的对应坐标
            x = int((j / new_width) * width)
            y = int((i / new_height) * height)
            # x = int((j / (new_width - 1)) * (pixels.shape[1] - 1))
            # y = int((i / (new_height - 1)) * (pixels.shape[0] - 1))
            # 找到最近的像素并放入新图像中
            new_pixels[i, j] = pixels[y, x]
            # if i < pixels.shape[0] and j < pixels.shape[1]:
            #   new_pixels[i, j] = pixels[y, x]

    return new_pixels.reshape(new_height, new_width)

# 对图像进行最临近插值
new_image = nearest_neighbor_interpolation(image, width*2, height*2)

# 显示原始图像、插值前图像和插值后图像的对比效果
fig, ax = plt.subplots(1, 3, figsize=(16, 8))
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original Image')
ax[1].imshow(new_image, cmap='gray')
ax[1].set_title('Interpolated Image')
ax[2].imshow(cv2.imread("lenna.png", cv2.IMREAD_GRAYSCALE), cmap='gray')
ax[2].set_title('Comparison Image')
plt.show()