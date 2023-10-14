n=int(input())
st=1
sp=n-1
for i in range(n):
    for j in range(st):
        print("*",end='')
    for j in range(sp):
        print("",end='')
    print()
    st=st+1
    sp=sp-1