class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        ps=0
        vs=0
        for i in range(1,len(nums)-1):
            if nums[i]> nums[i-1] and nums[i] > nums[i+1]:
                ps+=nums[i]
            elif nums[i]<nums[i-1] and nums[i] < nums[i+1]:
                vs+=nums[i]
        return ps-vs