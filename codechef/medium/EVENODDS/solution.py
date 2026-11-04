# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ml=0
    for i in range(n):
        oc=0
        for j in range(i,n):
            if a[j]%2!=0:
                oc+=1
            if oc%2==0:
                ml=max(ml,j-i+1)
    print(ml)