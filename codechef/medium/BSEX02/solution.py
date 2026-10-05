def main():
    # Write your code here
    t=int(input())
    for _ in range(t):
        n=int(input())
        p=1
        ans=0
        while n>=p:
            n-=p
            ans+=1
            p+=1
        print(ans)

if __name__ == "__main__":
    main()
