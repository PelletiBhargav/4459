n=int(input())
st=1
c=655
for i in range(n):
    for j in range(st):
        c=chr(c)
        print(c,end=' ')
        c=ord(c)+1 
    print()
    st=st+1 
    