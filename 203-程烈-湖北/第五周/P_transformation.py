import cv2
import numpy as np

img = cv2.imread('ayixia1.png')

result3 = img.copy()

'''
注意这里src和dst的输入并不是图像，而是图像对应的顶点坐标。
'''
src = np.float32([[15, 14], [13, 120], [750, 220], [750, 340]])
dst = np.float32([[0, 0], [0, 200], [800, 0], [800,200]])
print(img.shape)
# 生成透视变换矩阵；进行透视变换
# m = cv2.getPerspectiveTransform(src, dst)
import numpy as np

# 定义函数getPerspectiveTransform，用于计算透视变换矩阵
# 参数src为源点集，dst为目标点集
# src和dst的长度必须为4，否则抛出异常
# 构建线性方程组的系数矩阵A和常数向量B
# 将列表转换为numpy数组
# 使用最小二乘法求解线性方程组，得到透视变换矩阵H
# 返回H
def getPerspectiveTransform(src, dst):
    # src和dst的长度必须为4，否则抛出异常
    assert len(src) == 4 and len(dst) == 4, "输入的点集数量必须为4"
    A = []
    B = []
    # 构建线性方程组的系数矩阵A和常数向量B
    for i in range(4):
        x, y = src[i]
        u, v = dst[i]
        # 构建线性方程组的系数矩阵A和常数向量B
        A.append([x, y, 1, 0, 0, 0, -u*x, -u*y])
        A.append([0, 0, 0, x, y, 1, -v*x, -v*y])
        B.append(u)
        B.append(v)
    # 将列表转换为numpy数组
    A = np.array(A)
    B = np.array(B)
    # 使用最小二乘法求解线性方程组，得到透视变换矩阵H
    X, _, _, _ = np.linalg.lstsq(A, B, rcond=None)
    H = np.array([[X[0], X[1], X[2]], [X[3], X[4], X[5]], [X[6], X[7], 1]])
    return H
#
# # 示例
# src = np.float32([[0, 0], [1, 0], [1, 1], [0, 1]])
# dst = np.float32([[0, 0], [2, 0], [2, 2], [0, 2]])
# H = getPerspectiveTransform(src, dst)
# print(H)

print("warpMatrix:")

result = cv2.warpPerspective(result3, H, (900, 300))
cv2.imshow("src", img)
cv2.imshow("result", result)
cv2.waitKey(0)
