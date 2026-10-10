class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        l=[]
        pp=0
        mp=float('-inf')
        ans=[-1,-1]
        for i in range(n):
            for j in range(n):
                if i!=j:
                    if nums[i]+nums[j]==target and nums[i]>nums[j]:
                        l.append([i,j])
        for i,j in l:
            pp=nums[i]*nums[j]
            if pp>mp:
                mp=pp
                ans[0]=i
                ans[1]=j
        return ans