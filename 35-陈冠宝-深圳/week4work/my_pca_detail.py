"""
使用PCA求样本矩阵X的K阶降维矩阵Z
"""
from sklearn.decomposition import PCA
import numpy as np
from sklearn import datasets #导入方法类
load_iris = datasets.load_iris() #加载iris数据集
# X = load_iris.data #加载特征数据

class CPCA(object):
    '''用PCA求样本矩阵X的K阶降维矩阵Z
    Note:请保证输入的样本矩阵X shape=(m, n)，m行样例，n个特征
    '''

    def __init__(self, X, K):
        '''
        :param X,训练样本矩阵X
        :param K,X的降维矩阵的阶数，即X要特征降维成k阶
        '''
        self.X = X  # 样本矩阵X
        self.K = K  # K阶降维矩阵的K值
        self.centrX = []  # 矩阵X的中心化
        self.C = []  # 样本集的协方差矩阵C
        self.U = []  # 样本矩阵X的降维转换矩阵
        self.Z = []  # 样本矩阵X的降维矩阵Z


        self.centrX = self._centralized()
        self.C = self._cov()
        self.U = self._U()
        self.Z = self._Z()  # Z=XU求得

    # 中心化（零均值化）过程得到中心化矩阵
    def _centralized(self):
        '''矩阵X的中心化'''
        # print('样本矩阵X:\n', self.X)
        centrX = []
        mean = np.array([np.mean(attr) for attr in self.X.T])  # 样本集的特征均值
        # print('样本集的特征均值:\n', mean)
        centrX = self.X - mean  ##样本集的中心化，每一维度数据减去该维度所在的平均值
        # print('样本矩阵X的中心化centrX:\n', centrX)
        return centrX

    # 求中心化后的数据的协方差矩阵，
    def _cov(self):
        '''求样本矩阵X的协方差矩阵C'''
        # 样本集的样例总数
        ns = np.shape(self.centrX)[0]
        # 样本矩阵的协方差矩阵C，矩阵转置和矩阵点乘除以（维度数减一）
        C = np.dot(self.centrX.T, self.centrX) / (ns - 1)
        # print('样本矩阵X的协方差矩阵C:\n', C)
        return C

    # 由np.linalg.eig得到特征值和特征向量，对特征值排序，并将对于的特征向量组合而成降维矩阵
    def _U(self):
        '''求X的降维转换矩阵U, shape=(n,k), n是X的特征维度总数，k是降维矩阵的特征维度'''
        # 先求X的协方差矩阵C的特征值和特征向量
        a, b = np.linalg.eig(self.C)  # 特征值赋值给a，对应特征向量赋值给b。函数doc：https://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.linalg.eig.html
        # print('样本集的协方差矩阵C的特征值:\n', a)
        # print('样本集的协方差矩阵C的特征向量:\n', b)
        # 给出特征值降序的topK的索引序列
        ind = np.argsort(-1 * a)
        # 构建K阶降维的降维转换矩阵U
        UT = [b[:, ind[i]] for i in range(self.K)]
        U = np.transpose(UT)
        # print('%d阶降维转换矩阵U:\n' % self.K, U)
        return U

    def _Z(self):
        '''按照Z=XU求降维矩阵Z, shape=(m,k), n是样本总数，k是降维矩阵中特征维度总数'''
        Z = np.dot(self.X, self.U)
        # print('X shape:', np.shape(self.X))
        # print('U shape:', np.shape(self.U))
        # print('Z shape:', np.shape(Z))
        # print('样本矩阵X的降维矩阵Z:\n', Z)
        return Z


if __name__ == '__main__':
    '10样本4维特征的样本集, 行为样例，列为特征维度'
    X = load_iris.data  # 加载特征数据
    K = np.shape(X)[1]-2
    # print('样本集(10行4列，10个样例，每个样例4个特征):\n', X)
    mypca = CPCA(X, K)
    # print('原始数据X shape:', np.shape(pca.X))
    # print('降维矩阵U shape:', np.shape(pca.U))
    # print('降维数据Z shape:', np.shape(pca.Z))
    print('detail降维数据Z\n\n', mypca.Z)
    cX=mypca.centrX
    klearnpca = PCA(n_components=2)  # 设置降到2维
    newcX = klearnpca.fit_transform(cX)  # 训练并得到降维后的数据
    print('中心化后klearn降维数据Z\n\n', mypca.Z)