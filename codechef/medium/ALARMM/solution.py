# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    c1=0
    ans=0
    for i in s:
        if i==1:
            c1+=1 
    if k=0:
        ans+=c1
    