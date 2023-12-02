import numpy as np
import matplotlib.pyplot as plt

def kmeans(data, k, max_iter=100):
    # 随机初始化聚类中心
    centroids = data[np.random.choice(range(len(data)), k, replace=False)]

    for _ in range(max_iter):
        # 计算每个数据点到聚类中心的距离
        distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=-1)

        # 将数据点分配到最近的聚类中心
        labels = np.argmin(distances, axis=-1)

        # 更新聚类中心
        new_centroids = np.array([data[labels == i].mean(axis=0) for i in range(k)])

        # 如果聚类中心没有变化，提前结束迭代
        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids

    return labels, centroids

# 示例
data = np.array([[1, 6], [2, 4], [1, 3], [5, 2], [8, 4], [9, 0]])
k = 2
labels, centroids = kmeans(data, k)

# 绘制数据点
plt.scatter(data[:, 0], data[:, 1], c=labels)

# 绘制聚类中心
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x')

plt.show()
