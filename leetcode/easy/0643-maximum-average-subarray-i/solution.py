class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        cs=0
        for i in range(k):
            cs+=nums[i]
        ms=cs
        for i in range(k,len(nums)):
            cs+=nums[i]
            cs-=nums[i-k]
            if cs>ms:
                ms=cs
        return ms/k