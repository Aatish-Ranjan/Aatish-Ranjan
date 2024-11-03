# We want to do matrix multiplication of two matrix.
# the approach to solve this problem is:
#       initialize an empty matrix of desired dimension with zero.
#       pick ith row and jth column as a list.
#       dot product if the list (ith row and jth column).

def initialize_c(dim):
    c=[]
    for i in range(dim):
        c.append([])
        for j in range(dim):
            c[i].append(0)
    return c

def row(M,i):
    l=[]
    for a in range(len(M)):
        l.append(M[i][a])
    return l

def column(M,j):
    l=[]
    for k in range(len(M)):
        l.append(M[k][j])
    return l

def dot_product(r,c):
    ans=0
    for i in range(len(r)):
        ans=ans+r[i]*c[i]
    return ans

def matrix_mul(M,N):
    dim=len(M)
    c=initialize_c(dim)
    for i in range(dim):
        for j in range(dim):
            c[i][j]=dot_product(row(M,i),column(N,j))
    return c

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[1,2,3],[1,2,3]]

print(matrix_mul(a,b))