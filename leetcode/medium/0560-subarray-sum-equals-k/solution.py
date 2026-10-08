class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        f={0:1}
        ps=0
        c=0
        for i in nums:
            ps+=i
            d=ps-k
            if d in f:
                c+=f[d]
            if ps in f:
                f[ps]+=1
            else:
                f[ps]=1   
        return c