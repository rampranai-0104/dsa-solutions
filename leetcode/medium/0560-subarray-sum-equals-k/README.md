# Subarray Sum Equals K

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of integers `nums` and an integer `k`, return  *the total number of subarrays whose sum equals to*  `k`.

A subarray is a contiguous  **non-empty**  sequence of elements within an array.

 

 **Example 1:** 

```
Input: nums = [1,1,1], k = 2
Output: 2

```

 **Example 2:** 

```
Input: nums = [1,2,3], k = 3
Output: 2

```

 

 **Constraints:** 

- 1 <= nums.length <= 2 * 104
- -1000 <= nums[i] <= 1000
- -107 <= k <= 107

## Solution

**Language:** Python  
**Runtime:** 32 ms (beats 59.11%)  
**Memory:** 21.8 MB (beats 57.38%)  
**Submitted:** 2026-10-08T14:47:30.821Z  

```py
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        f={0:1}
        ps=0
        c=0
        for i in nums:
            ps+=i
            d=ps-k
            if d in f:
                c+=f[d]
            if ps in f:
                f[ps]+=1
            else:
                f[ps]=1   
        return c
```

---

[View on LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/)