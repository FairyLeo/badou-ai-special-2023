# 导入所需的库
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 加载鸢尾花数据集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 应用PCA
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# 训练模型
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_pca, y_train)

# 预测测试集
y_pred = knn.predict(X_test_pca)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy: ', accuracy)
