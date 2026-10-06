class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n=len(nums)
        l=[]
        s=0
        for i in range(n):
            s+=nums[i]
            l.append(s)
        return l