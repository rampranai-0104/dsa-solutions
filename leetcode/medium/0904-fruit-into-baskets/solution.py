class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        n=len(fruits)
        freq={}
        l=0
        r=0
        c=0
        for i in range(n):
            if fruits[i] not in freq:
                freq[fruits[i]]=1
            else:
                freq[fruits[i]]+=1
            r+=1
            while len(freq)>2:
                freq[fruits[l]]-=1
                if freq[fruits[l]]==0:
                    del freq[fruits[l]]
                l+=1
            c=max(c,r-l)
        return c
