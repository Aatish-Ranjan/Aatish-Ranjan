r1=[2,3,5]
r2=[6,3,8]
r3=[9,0,4]

s1=[4,5,2]
s2=[0,2,6]
s3=[7,1,4]

A=[]
B=[]

A.append(r1)
A.append(r2)
A.append(r3)

B.append(s1)
B.append(s2)
B.append(s3)

dim=3
c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            c[i][j]=c[i][j]+A[i][k]*B[k][j]
print(c)