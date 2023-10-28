import cv2
import matplotlib.pyplot as plt
# 读取图像文件并转换为灰度图像：

image_path = r"D:\BaiduNetdiskDownload\CV\lenna.png"
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 创建一个列表来存储不同阈值下的二值图像：

thresholds = [100, 128, 150, 200]
binary_images = []
# 对每个阈值进行二值化处理，并将结果存储在binary_images列表中：

for threshold in thresholds:
    _, binary_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)
    binary_images.append(binary_image)
# 创建一个新的figure对象，并设置其大小：

fig, axs = plt.subplots(2, 3, figsize=(10, 10))
# 在子图上分别显示原图、灰度图和不同阈值下的二值图像：

# 原图
axs[0, 0].imshow(image)
axs[0, 0].set_title('Original Image')
# 灰度图
axs[0, 1].imshow(gray_image, cmap='gray')
axs[0, 1].set_title('Grayscale Image')
# 二值图像（阈值100）
axs[0, 2].imshow(binary_images[0], cmap='gray')
axs[0, 2].set_title('Binary Image (Threshold 100)')
# 二值图像（阈值128）
axs[1, 0].imshow(binary_images[1], cmap='gray')
axs[1, 0].set_title('Binary Image (Threshold 128)')
# 二值图像（阈值150）
axs[1, 1].imshow(binary_images[2], cmap='gray')
axs[1, 1].set_title('Binary Image (Threshold 150)')
# 二值图像（阈值200）
axs[1, 2].imshow(binary_images[3], cmap='gray')
axs[1, 2].set_title('Binary Image (Threshold 200)')

plt.show()