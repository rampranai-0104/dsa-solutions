class Solution:
    def lengthOfLongestSubstring(self, a: str) -> int:
        n=len(a)
        seen=set()
        i=0
        j=0
        m=0
        while j<n and i<n:
            if a[j] not in seen:
                seen.add(a[j])
                j+=1
                m=max(m,j-i)
            else:
                seen.remove(a[i])
                i+=1
        return m
