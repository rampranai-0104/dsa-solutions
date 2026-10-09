# Q3. Max Consecutive Ones

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a binary array `nums`, return  *the maximum number of consecutive* `1` *'s in the array*.

 

 **Example 1:** 

```
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

```

 **Example 2:** 

```
Input: nums = [1,0,1,1,0,1]
Output: 2

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- nums[i] is either 0 or 1.

## Solution

**Language:** Python  
**Runtime:** 12 ms (beats 77.10%)  
**Memory:** 22.1 MB (beats 5.40%)  
**Submitted:** 2026-10-09T11:41:07.773Z  

```py
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        n=len(nums)
        c=0
        mc=0
        for i in range(n):
            if nums[i]==1:
                c+=1
                mc=max(c,mc)
            else:
                c=0
        return mc
```

---

[View on LeetCode](https://leetcode.com/problems/max-consecutive-ones/)