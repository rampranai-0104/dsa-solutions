class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, t: int) -> int:
        n=len(arr)
        c=0
        """for i in range(n-k+1):
            s=sum(arr[i:i+k]) 
            if s>=k*t:
                c+=1"""
        s=sum(arr[:k])
        if s>=k*t:
            c+=1
        for i in range(n-k):
            s-=arr[i]
            s+=arr[i+k]
            if s>=k*t:
                c+=1
        return c