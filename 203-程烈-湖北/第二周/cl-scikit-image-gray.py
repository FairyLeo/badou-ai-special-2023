import cv2
from skimage import io, exposure
import matplotlib.pyplot as plt

# 读取图像
image_path = r"D:\\BaiduNetdiskDownload\\CV\\lenna.png"
image = cv2.imread(image_path)

# 转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 二值化图像，使用不同的阈值
thresholds = [100, 128, 150, 200]
binary_images = []
for threshold in thresholds:
    _, binary_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)
    binary_images.append(binary_image)

# 创建图像显示网格
rows, cols = 2, len(thresholds) + 1
fig, axs = plt.subplots(rows, cols)

# 显示原图和灰度图像
axs[0, 0].imshow(image)
axs[0, 0].set_title('Original Image')
axs[0, 1].imshow(gray_image, cmap='gray')
axs[0, 1].set_title('Grayscale Image')

# 显示不同阈值的二值图像
for i, ax in enumerate(axs[1]):
    ax.imshow(binary_images[i], cmap='gray')
    ax.set_title(f'Binary Image with Threshold {thresholds[i]}')

# 显示图像网格
plt.show()
