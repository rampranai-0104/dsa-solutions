# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    m=a[0]
    c=0
    for i in a:
        c+=i 
        if i <m:
            m=i
    print(c-m)