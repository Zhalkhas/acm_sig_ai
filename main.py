A = []
a = []
B = []
b = []

size_matrix_1r = int(input())
size_matrix_2r = int(input())

size_matrix_1c = int(input())
size_matrix_2c = int(input())

if size_matrix_1c != size_matrix_2r:
    print("invalid input")

print("input matrix A")
try:
    while len(a) != size_matrix_1c:
        for i in range(size_matrix_1r):
            a = [int(x) for x in input().split()]
            if len(a) != size_matrix_1c:
                print("invalid input")
            A.append(a)
except IndexError:
    pass
print("input matrix B")
try:
    while len(b) != size_matrix_2c:
        for i in range(size_matrix_2r):
            b = [int(x) for x in input().split()]
            if len(b) != size_matrix_2c:
                print("invalid input")
            B.append(b)
except IndexError:
    pass

result = [[0 for x in range(size_matrix_2c)] for i in range(size_matrix_1r)]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            try:
                result[i][j]+=A[i][k]*B[k][j]
            except IndexError:
                pass

for i in result:
    print(i)