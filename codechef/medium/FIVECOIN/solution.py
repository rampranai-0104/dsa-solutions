# cook your dish here
n=int(input())
ans=0
rem=n
if n>=5:
    ans+=1
    rem=n-5 
print(ans+rem)