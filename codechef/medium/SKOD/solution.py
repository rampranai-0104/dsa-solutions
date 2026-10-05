# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    m=a[0]
    c=0
    for i in a:
        if i<m:
            m=i
    for i in a:
        if i!=m:
            c+=i 
        else:
            c+=0
    print(c)