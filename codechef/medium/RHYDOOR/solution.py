# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    c=1
    do=0
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            c+=1 
            if c==3:
                do+=1 
                c=1
        else:
            c=1 
    print(do)