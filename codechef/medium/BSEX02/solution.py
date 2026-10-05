def main():
    # Write your code here
    t=int(input())
    for _ in range(t):
        n=int(input())
        p=1
        ans=0
        while n>0:
            n=n-p
            p+=1
            if p>n:
                ans=p-1
        print(ans)

if __name__ == "__main__":
    main()
