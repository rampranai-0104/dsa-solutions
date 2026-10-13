# Product of Array Except Self

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums`, return  *an array*  `answer`  *such that*  `answer[i]`  *is equal to the product of all the elements of*  `nums`  *except*  `nums[i]`.

The product of any prefix or suffix of `nums` is  **guaranteed**  to fit in a  **32-bit**  integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

 

 **Example 1:** 

```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

```

 **Example 2:** 

```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

```

 

 **Constraints:** 

- 2 <= nums.length <= 105
- -30 <= nums[i] <= 30
- The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

 

 **Follow up:**  Can you solve the problem in `O(1)` extra space complexity? (The output array  **does not**  count as extra space for space complexity analysis.)

## Solution

**Language:** Python  
**Runtime:** 35 ms (beats 25.17%)  
**Memory:** 27.9 MB (beats 7.68%)  
**Submitted:** 2026-10-13T14:45:13.514Z  

```py
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        lp=[1]*n
        rp=[1]*n
        for i in range(1,n):
            lp[i]=lp[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            rp[i]=rp[i+1]*nums[i+1]
        res=[1]*n
        for i in range(n):
            res[i]=lp[i]*rp[i]
        return res
```

---

[View on LeetCode](https://leetcode.com/problems/product-of-array-except-self/)