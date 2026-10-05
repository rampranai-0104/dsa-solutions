class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        m=[]
        intervals.sort(key=lambda x:x[0])
        p=intervals[0]
        for i in intervals[1:]:
            if i[0]<=p[1]:
                p[1]=max(p[1],i[1])
            else:
                m.append(p)
                p=i 
        m.append(p)
        return m