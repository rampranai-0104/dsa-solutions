def main():
    # Write your code here
    t=int(input())
    for _ in range(t):
        n=int(input())
        p=1
        c=0
        ans=0
        for i in range(n,-1,-1):
            c=i-p
            p+=1 
            if c<0:
                ans=p-1 
        print(ans)
            

if __name__ == "__main__":
    main()
