import numpy as np
import cv2
import matplotlib.pyplot as plt

# 读取图片
img = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)

# 定义函数，输入参数为sigma、mean和噪音比例
def add_gaussian_noise(img, sigma, mean, ratio):
    noise = np.random.normal(mean, sigma, img.shape).astype(np.uint8)
    img_noisy = np.clip(img + noise * ratio, 0, 255)
    return img_noisy

# 生成高斯随机数
sigma = 25
mean = 0

# 添加不同比例的高斯噪音
img_25 = add_gaussian_noise(img, sigma, mean, 0.25)
img_50 = add_gaussian_noise(img, sigma, mean, 0.50)
img_75 = add_gaussian_noise(img, sigma, mean, 0.75)

# 显示原始图片和添加了不同比例高斯噪音的图片
plt.figure()
plt.subplot(221), plt.imshow(img, cmap='gray'), plt.title('Original Image')
plt.subplot(222), plt.imshow(img_25, cmap='gray'), plt.title('Image with 25% Noise')
plt.subplot(223), plt.imshow(img_50, cmap='gray'), plt.title('Image with 50% Noise')
plt.subplot(224), plt.imshow(img_75, cmap='gray'), plt.title('Image with 75% Noise')
plt.show()
