import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt

# =====================第一部分 NumPy数组基础操作====================
# 1.创建一维、二维、三维数组
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("一维数组：")
print(arr1)
print("二维数组：")
print(arr2)
print("三维数组：")
print(arr3)

# 2.数组索引、切片
print("\n一维数组索引：",arr1[2])
print("一维数组切片：",arr1[1:4])
print("二维数组索引：",arr2[1,2])
print("二维数组切片：")
print(arr2[0:2,:])

# 3.形状变换
print("\n原二维数组形状：",arr2.shape)
arr_reshape = arr2.reshape(9,1)
print("变换后形状：",arr_reshape.shape)

# 4.矩阵运算函数：加法、乘法、转置
def mat_add(a,b):
    return a + b

def mat_mul(a,b):
    return a @ b

def mat_trans(a):
    return a.T

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print("\n矩阵相加：")
print(mat_add(A,B))
print("矩阵相乘：")
print(mat_mul(A,B))
print("矩阵转置：")
print(mat_trans(A))

# 5.随机数据统计分析
rand_data = np.random.randn(20)
print("\n随机数组：")
print(rand_data)
print("均值：",np.mean(rand_data))
print("方差：",np.var(rand_data))
print("最大值：",np.max(rand_data))
print("最小值：",np.min(rand_data))

# =====================第二部分 金融数据分析实战====================
# 1.生成模拟股票数据
np.random.seed(10)
price = np.cumsum(np.random.randn(100)) + 100

# 2.计算日收益率、年化波动率
returns = np.diff(price) / price[:-1]
volatility = np.std(returns) * np.sqrt(252)
print("\n年化波动率：%.4f"%volatility)

# 3.5日、20日移动平均线
win5 = 5
win20 = 20
ma5 = np.convolve(price, np.ones(win5)/win5, mode="valid")
ma20 = np.convolve(price, np.ones(win20)/win20, mode="valid")

# 4.投资组合：方差、协方差
stock1 = returns
stock2 = np.roll(returns,1)
cov_matrix = np.cov(stock1,stock2)
print("\n协方差矩阵：")
print(cov_matrix)

# 5.绘图可视化
plt.figure(figsize=(10,4))
plt.plot(price,label="stock price")
plt.plot(ma5,label="MA5")
plt.plot(ma20,label="MA20")
plt.legend()
plt.title("Stock Price and Moving Average")
plt.show()