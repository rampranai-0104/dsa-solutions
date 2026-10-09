class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        n=len(nums)
        c=0
        mc=0
        for i in range(n):
            if nums[i]==1:
                c+=1
                mc=max(c,mc)
            else:
                c=0
        return mc