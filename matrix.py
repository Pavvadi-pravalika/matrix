# matrix sum

# mat1 = [
#     [1,5,67],
#     [2.2,3,-2],
#     [4,9,10],
#     [5,3,-3]
#     ]
# sum=0
# for i in mat1:
#     # print(str(i))
#     for j in i:
#         # print(str(j))
#         sum += j
# print(sum)


# Transpose of matrix:
# mat1 = [
#     [1,5,67],
#     [2.2,3,-2],
#     [4,9,10]
#     # [5,3,-3]
#     ]
# for i in range(len(mat1)):
#     for j in range(i):
#         mat1[i][j],mat1[j][i]=mat1[j][i], mat1[i][j]

# print(mat1)
# 1. Diagonal elements sum (Level 1 is any one diagonal and level 2 is )
matrix1 = [[1, 5, 6], [2.2, 3, -2], [4, 9, 10]]
matrix2 = [[2, 4, 1], [1.8, -3, 2], [6, -1, 5]]

diagonal_sum = 0

for i in range(len(matrix1)):
    diagonal_sum += matrix1[i][i] + matrix2[i][i] 

print("Diagonal Sum:", diagonal_sum)


# 2. Add 2 matrixes
matrix3 = [[1, 5, 6], [2.2, 3, -2], [4, 9, 10]]
matrix4 = [[2, 4, 1], [1.8, -3, 2], [6, -1, 5]]

result = []

for i in range(len(matrix3)):
    row = []
    for j in range(len(matrix3[i])):
        row.append(matrix3[i][j] + matrix4[i][j])
    result.append(row)

print(result)