import warnings
warnings.filterwarnings("ignore")
warnings.simplefilter(action="ignore", category=FutureWarning)

import numpy as np
import time

#练习1
#任务1
A = np.random.rand(1000, 2000)
B = np.random.rand(2000, 3000)

start1 = time.time()
res1 = np.dot(A, B)
t1 = time.time() - start1

start2 = time.time()
res2 = A @ B
t2 = time.time() - start2

start3 = time.time()
res3 = np.matmul(A, B)
t3 = time.time() - start3

print("====矩阵乘法耗时对比====")
print(f"np.dot耗时：{t1:.2f} s")
print(f"@运算符耗时：{t2:.2f} s")
print(f"np.matmul耗时：{t3:.2f} s")

#任务2
arr_c = np.random.rand(1000, 1000, order="C")
arr_f = np.random.rand(1000, 1000, order="F")

start_c_row = time.time()
arr_c.sum(axis=1)
t_c_row = time.time() - start_c_row

start_f_row = time.time()
arr_f.sum(axis=1)
t_f_row = time.time() - start_f_row

start_c_col = time.time()
arr_c.sum(axis=0)
t_c_col = time.time() - start_c_col

start_f_col = time.time()
arr_f.sum(axis=0)
t_f_col = time.time() - start_f_col

print("\n====内存布局求和耗时====")
print(f"C顺序 行求和：{t_c_row:.4f} s，列求和：{t_c_col:.4f} s")
print(f"F顺序 行求和：{t_f_row:.4f} s，列求和：{t_f_col:.4f} s")

#任务3
A_small = np.random.rand(800, 800)
result = np.empty_like(A_small)
temp = np.empty_like(A_small)

np.multiply(A_small, A_small, out=result)
np.multiply(2, A_small, out=temp)
np.add(result, temp, out=result)
np.add(result, 1, out=result)

print("\n====表达式计算完成====")
print("A²+2*A+1 计算完毕")

#练习2
#任务1
prices = np.array([100, 102, 105, 103, 107])
returns = np.log(prices[1:] / prices[:-1])
print("\n====每日对数收益率====")
print(returns)

#任务2
price_data = np.random.rand(100) * 20 + 10

win5 = 5
ma5 = np.convolve(price_data, np.ones(win5)/win5, mode="valid")
win20 = 20
ma20 = np.convolve(price_data, np.ones(win20)/win20, mode="valid")

print("\n====移动平均线数据====")
print("5日均线前5个值：", ma5[:5])
print("20日均线前5个值：", ma20[:5])

#任务3
rate_data = np.random.randn(1000, 252) * 0.02
volatility = rate_data.std(axis=1) * np.sqrt(252)
corr_matrix = np.corrcoef(rate_data)

print("\n====风险分析结果====")
print("前5只股票年化波动率：", volatility[:5])
print("相关系数矩阵形状：", corr_matrix.shape)