import numpy as np
from sklearn.datasets import load_iris


# 加载鸢尾花数据集
iris = load_iris()
X = iris.data

# 计算数据的均值和协方差矩阵
mean = np.mean(X, axis=0)
cov_matrix = np.cov(X.T)

# linalg对协方差矩阵进行特征值分解，返回一个元组,得到特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# 根据特征值的大小，选择前k个最大的特征值对应的特征向量，组成投影矩阵
#从特征向量矩阵中选择前k个特征向量。在NumPy中，冒号表示选择所有行或列，所以:表示选择所有行，:k表示选择前k行
k = 3
projection_matrix = eigenvectors[:, :k]
# @符号用于执行矩阵乘法
# 将原始数据投影到投影矩阵上，得到降维后的数据
X_pca = X @ projection_matrix

print("原数据：", X)
print("降维后的数据：", X_pca)
