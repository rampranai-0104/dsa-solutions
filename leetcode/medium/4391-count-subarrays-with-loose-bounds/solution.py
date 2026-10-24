class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        l=[]
        for i in range(len(nums)):
            l.append(nums[i])
        c=0
        li=-1
        for i in range(len(l)):
            num=l[i]
            if num<minK or num>maxK:
                li=i
            else:
                c+=i-li
        return c