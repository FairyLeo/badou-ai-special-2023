import cv2

# 读取图片
image = cv2.imread('_MG_8178.jpg', cv2.IMREAD_GRAYSCALE)

# 应用Canny算法
edges = cv2.Canny(image, 20, 90)

# 显示原始图片和边缘检测后的图片
cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Canny Edge Detection', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Original Image', image.shape[1], image.shape[0])
cv2.resizeWindow('Canny Edge Detection', edges.shape[1], edges.shape[0])
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 等待按键，然后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()