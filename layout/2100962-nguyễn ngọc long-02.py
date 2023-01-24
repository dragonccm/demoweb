def Max(a,b):
    if b is None:
        return a
    if a>b:
        return a
    else:
        return b
     
def find_max(L,G,i):
    if i < 0:
        return
    G[len(L)-1] =  L[i]
    while(i>-1):
        if (L[i] in L[i+1:len(L)]):
            k = L[i+1:].index(L[i]) + (i+1)
            X = L[i]*2 +G[k+1]
        else:
            X = L[i]
        G[i] = Max(X,G[i+1])
        i-=1
L = []
n = int(input('nhap so lượng quà'))
for i in range(0,n):
    L.append(int(input("mời chon quà")))
G=[0]*(n+1)
find_max(L,G,n-1)
print("giá trị phần quà lớn nhất có thể chọn là")
print(G[0])