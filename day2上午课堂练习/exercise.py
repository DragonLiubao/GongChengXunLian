import numpy as np

#练习1：数组创建与形状操作
arr = np.random.randint(0, 10, size=(3, 4))
reshaped_arr = arr.reshape(4, 3).T
filtered_arr = arr[arr > 5]

print("练习1")
print(arr)
print(reshaped_arr)
print(filtered_arr)

#练习2：索引与切片
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
row2 = arr[1, 0:3]
col3 = arr[:, 2]
odd_row = arr[::2, :]

print("\n练习2")
print(row2)
print(col3)
print(odd_row)

#练习3：矢量化运算与聚合函数
A = np.random.randint(1, 6, size=(2, 3))
B = np.random.randint(1, 6, size=(2, 3))
elem_mul = A * B
mat_mul = A @ B.T

c = np.array([[1, 2], [3, 4]])
sum_row = np.sum(c, axis=1)
sum_col = np.sum(c, axis=0)

d = np.array([1.2, 3.5, 2.8])
mean_d = np.mean(d)
std_d = np.std(d)
round_d = np.round(d)

print("\n练习3")
print(elem_mul)
print(mat_mul)
print(sum_row)
print(sum_col)
print(mean_d)
print(std_d)
print(round_d)

#练习4：综合应用
rand_arr = np.random.rand(10)
norm_arr = (rand_arr - rand_arr.min()) / (rand_arr.max() - rand_arr.min()) * 100
cumsum_arr = np.cumsum(norm_arr)
cummax_arr = np.maximum.accumulate(norm_arr)

print("\n练习4")
print(norm_arr)
print(cumsum_arr)
print(cummax_arr)