import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取原始灰度图像
image = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)

# 计算灰度直方图H
hist, bins = np.histogram(image.flatten(), 256, [0, 256])

# 计算累加直方图
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

# 根据累加直方图和直方图均衡化原理得到输入与输出之间的映射关系
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')

# 根据映射关系得到结果：dst(x,y) = H'(src(x,y))进行图像变换
dst = cdf[image]

# 计算均衡化后的直方图
equalized_hist, equalized_bins = np.histogram(dst.flatten(), 256, [0, 256])

# 显示原图及其对应的直方图
plt.figure()
plt.subplot(121)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.subplot(122)
plt.plot(hist)
plt.title('Histogram')

# 显示均衡化后的图片及直方图,一个figure只能显示一张直方图
plt.figure()
plt.subplot(121)
plt.imshow(dst, cmap='gray')
plt.title('Equalized Image')
plt.subplot(122)
plt.plot(equalized_hist)
plt.title('Equalized Histogram')

plt.show()
