# cook your dish here
t=int(input())
for _ in range(t):
    m,x,y=map(int,input().split())
    a=list(map(int,input().split()))
    r=x*y   
    h=[0]*100
    for i in range(m):
        l=max(1,a[i]-r)
        u=min(100,a[i]+r)
        for j in range(l-1,u):
            h[j]=1
    ans=h.count(0)
    print(ans)