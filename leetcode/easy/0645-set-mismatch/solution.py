class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n=len(nums)
        s=set()
        d=0
        m=0
        for i in nums:
            if i in s:
                d=i
            s.add(i)
        for i in range(1,n+1):
            if i not in s:
                m=i
                break

        return [d,m]