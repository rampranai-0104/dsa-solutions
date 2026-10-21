# cook your dish here
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    p=0
    g=0
    for x in a:
        p+=x 
        hs=p*(p-1) //2
        if hs<=m:
            g+=1 
        else:
            break
    print(g)