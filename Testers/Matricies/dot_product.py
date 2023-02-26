import numpy as np
from decimal import Decimal

A = np.array([[1, 2], [3, 4]])
B = np.asmatrix(A)

# print(A)
# print(B)
# print('B:', B, '\n')
# print('T(B):', B.transpose(), '\n')
# print('B * T(B):', B * B.transpose())
#print(np.dot(B, B))

#print(np.linalg.det(B))

#print(np.linalg.eigvals(B))
#print(np.linalg.eig(B))

#print(u"B\u20D7")

# Solving matricies
R = np.array(
    [[1, 2],
     [3, 4]]
)

P = np.array(
    [1, 3.6]
)

print(R)
print(P)
result = np.linalg.solve(R, P)
output = ''
for num in enumerate(result):
    x_val = 'x\u20D7'
    if (num[1]) > 0:
        output += f'+ {round(num[1], 10)}*({x_val}{num[0]+1}) '
    else:
        output += f'- {abs(round(num[1], 10))}*({x_val}{num[0]+1}) '

print(output)
