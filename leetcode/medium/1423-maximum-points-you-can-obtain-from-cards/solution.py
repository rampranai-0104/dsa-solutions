class Solution:
    def maxScore(self, a: list[int], k: int) -> int:
        n=len(a)
        i=0
        j=n-1
        ans=0
        l=a[:k]
        ll=len(l)
        ans=sum(l)
        m=ans
        for i in range(ll):
            #m=max(m,ans)
            ans-=l[k-i-1]
            l.append(a[n-i-1])
            ans+=a[n-i-1]
            m=max(m,ans)
        return m
    