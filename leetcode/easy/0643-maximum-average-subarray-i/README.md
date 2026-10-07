# Maximum Average Subarray I

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose  **length is equal to**  `k` that has the maximum average value and return  *this value*. Any answer with a calculation error less than `10-5` will be accepted.

 

 **Example 1:** 

```
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

```

 **Example 2:** 

```
Input: nums = [5], k = 1
Output: 5.00000

```

 

 **Constraints:** 

- n == nums.length
- 1 <= k <= n <= 105
- -104 <= nums[i] <= 104

## Solution

**Language:** Python  
**Runtime:** 47 ms (beats 92.41%)  
**Memory:** 29.2 MB (beats 53.82%)  
**Submitted:** 2026-10-07T15:49:34.616Z  

```py
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        cs=0
        for i in range(k):
            cs+=nums[i]
        ms=cs
        for i in range(k,len(nums)):
            cs+=nums[i]
            cs-=nums[i-k]
            if cs>ms:
                ms=cs
        return ms/k
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-average-subarray-i/)