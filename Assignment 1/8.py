def print_mat(mat,n):
    print(' ')
    for i in range(n):
        for j in range(n):
            print(mat[i][j],end = ' ')
        print(' ')

def LU(mat,n):
    l = [[0 for i in range(0, n)] for i in range(0, n)]
    u = [[0 for i in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for k in range(i, n):
            add = 0
            for j in range(i):
                add += (l[i][j] * u[j][k]);
            u[i][k] = mat[i][k] - add;

        for k in range(i, n):
            if (i == k):
                l[i][i] = 1
            else:
                sum = 0
                for j in range(i):
                    sum += (l[k][j] * u[j][i])
                l[k][i] = int((mat[k][i] - sum) / u[i][i])
    print('\nL = ')            
    print_mat(l,n)
    print('\nU = ')
    print_mat(u,n)
    
n = int(input('Enter order of matrix'))

print('Enter the matrix')
print()

l= []
mat = []
for i in range(n):
    l = list(map(int,input().split()))
    mat.append(l)
LU(mat,n)
