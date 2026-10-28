# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    ans=0
    p=0
    i=0
    while i<n:
        if s[i]=='1' and i>=p:
            po=min(n-1,i+k)
            ans+=1 
            p=po+1 
        i+=1 
    print(ans)
        