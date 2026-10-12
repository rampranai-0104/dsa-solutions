# Check if All the Integers in a Range Are Covered

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given a 2D integer array `ranges` and two integers `left` and `right`. Each `ranges[i] = [starti, endi]` represents an  **inclusive**  interval between `starti` and `endi`.

Return `true`  *if each integer in the inclusive range*  `[left, right]`  *is covered by  **at least one**  interval in*  `ranges`. Return `false`  *otherwise*.

An integer `x` is covered by an interval `ranges[i] = [starti, endi]` if `starti <= x <= endi`.

 

 **Example 1:** 

```
Input: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
Output: true
Explanation: Every integer between 2 and 5 is covered:
- 2 is covered by the first range.
- 3 and 4 are covered by the second range.
- 5 is covered by the third range.

```

 **Example 2:** 

```
Input: ranges = [[1,10],[10,20]], left = 21, right = 21
Output: false
Explanation: 21 is not covered by any range.

```

 

 **Constraints:** 

- 1 <= ranges.length <= 50
- 1 <= starti <= endi <= 50
- 1 <= left <= right <= 50

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.4 MB (beats 30.93%)  
**Submitted:** 2026-10-12T15:20:37.565Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/)