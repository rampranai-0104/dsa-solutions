# cook your dish here
t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in a:
        c+=i 
    if c%2==0:
        ans=c//2
    else:
        ans=-1 
    print(abs(ans))
    t-=1