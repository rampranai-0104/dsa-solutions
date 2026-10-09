class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i=0
        j=n
        l=[]
        while i<n and j < 2*n:
            l.append(nums[i])
            l.append(nums[j])
            i+=1
            j+=1
        return l
