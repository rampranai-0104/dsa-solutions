class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        n=len(ranges)
        m=len(ranges[0])
        for i in range(left,right+1):
            c=False
            for s,e in ranges:
                if s<=i<=e:
                    c=True
                    break
            if not c:
                return False
        return True