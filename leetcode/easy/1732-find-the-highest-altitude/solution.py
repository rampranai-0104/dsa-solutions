class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        n=len(gain)
        s=0
        ans=0
        for i in range(n):
            s+=gain[i]
            ans=max(s,ans)
        return ans