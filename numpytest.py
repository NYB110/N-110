import numpy as np
import  torch
# 创建数组
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
x = torch.tensor([-1.0, 0.0, 1.0])
print('张量：',x)
print("Original 2D Array:\n", arr_2d)

# 数组变换
# 转置
arr_2d_t = arr_2d.T
# 扁平化
arr_flat = arr_2d.flatten()
# 重塑
arr_reshaped = arr_flat.reshape((3, 3))
# 切片
slice_arr = arr_2d[1:3, 1:3]
# 索引
element = arr_2d[1, 1]
# 广播
arr_broadcast = arr_1d + 10  # 每一个元素都加10
# 数组拼接
arr_stacked_v = np.vstack((arr_2d, arr_2d + 10))
arr_stacked_h = np.hstack((arr_2d, arr_2d + 10))
# 数组条件筛选
filtered_arr = arr_2d[arr_2d > 5]
# 数组排序
sorted_arr = np.sort(arr_2d, axis=0)
# 线性代数
# 点积
dot_product = np.dot(arr_2d, arr_2d.T)
# 特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(dot_product)
# 矩阵逆
if np.linalg.det(arr_2d) != 0:
    inv_arr = np.linalg.inv(arr_2d)
# 随机数组
rand_arr = np.random.rand(3, 4)
# 统计函数
mean_val = np.mean(arr_2d)
std_dev = np.std(arr_2d)
# 数组条件赋值
arr_2d[arr_2d > 5] = 0
# 数组迭代
for row in arr_2d:
    print(row)
# 更多操作可以继续添加...

# 打印一些结果

print("Transposed 2D Array:\n", arr_2d_t)
print("Flattened Array:\n", arr_flat)
print("Reshaped Array:\n", arr_reshaped)
print("Sliced Array:\n", slice_arr)
print("Element at [1, 1]:", element)
print("Broadcast Array:\n", arr_broadcast)
print("Vertically Stacked Array:\n", arr_stacked_v)
print("Horizontally Stacked Array:\n", arr_stacked_h)
print("Filtered Array:\n", filtered_arr)
print("Sorted Array:\n", sorted_arr)
print("Dot Product:\n", dot_product)
print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
if np.linalg.det(arr_2d) != 0:

 print("Random Array:\n", rand_arr)
print("Mean Value:", mean_val)
print("Standard Deviation:", std_dev)
print("Modified Array:\n", arr_2d)
