import cv2
import numpy as np
from matplotlib import pyplot as plt

def add_salt_pepper_noise(image, snr, pixel_value_ratio):
    height, width = image.shape[:2]
    SP = height * width
    NP = int(SP * snr)

    for _ in range(NP):
        i = np.random.randint(height)
        j = np.random.randint(width)
        if np.random.rand() < pixel_value_ratio:
            image[i, j] = 255
        else:
            image[i, j] = 0

    return image

# 读取图像并获取其尺寸
image = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)
height, width = image.shape[:2]

# 按给定的信噪比和像素值比例添加椒盐噪声
snr_values = [0.25, 0.5, 0.75]
pixel_value_ratios = [0.25, 0.5, 0.75]
images_with_noise = []

for snr in snr_values:
    for pixel_value_ratio in pixel_value_ratios:
        noisy_image = add_salt_pepper_noise(image, snr, pixel_value_ratio)
        images_with_noise.append(noisy_image)

# 显示原始图像和添加噪声后的图像
titles = ['Original', 'SNR=25%', 'SNR=50%', 'SNR=75%']
images = [image] + images_with_noise
for i in range(len(images)):
    plt.subplot(1, len(images), i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.show()
