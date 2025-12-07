# 二维数组操作示例

# 1. 创建二维数组
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("初始矩阵:")
for row in matrix:
    print(row)

# 2. 添加一行
matrix.append([10, 11, 12])
print("\n添加一行后:")
for row in matrix:
    print(row)

# 3. 在指定位置插入一行
matrix.insert(1, [13, 14, 15])
print("\n在索引1处插入新行后:")
for row in matrix:
    print(row)

# 4. 给某行添加元素
matrix[0].append(99)
print("\n给第一行添加元素后:")
for row in matrix:
    print(row)

# 5. 使用NumPy操作二维数组
try:
    import numpy as np
    
    print("\n使用NumPy操作:")
    np_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("原始NumPy数组:")
    print(np_matrix)
    
    # 添加一行
    np_matrix = np.vstack([np_matrix, [10, 11, 12]])
    print("\n添加一行后:")
    print(np_matrix)
    
    # 添加一列
    np_matrix = np.hstack([np_matrix, [[13], [14], [15], [16]]])
    print("\n添加一列后:")
    print(np_matrix)
    
except ImportError:
    print("\n未安装NumPy，跳过NumPy示例")