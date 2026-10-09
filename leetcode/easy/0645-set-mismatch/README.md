# Q1. Set Mismatch

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You have a set of integers `s`, which originally contains all the numbers from `1` to `n`. Unfortunately, due to some error, one of the numbers in `s` got duplicated to another number in the set, which results in  **repetition of one**  number and  **loss of another**  number.

You are given an integer array `nums` representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return  *them in the form of an array*.

 

 **Example 1:** 

```
Input: nums = [1,2,2,4]
Output: [2,3]

```

 **Example 2:** 

```
Input: nums = [1,1]
Output: [1,2]

```

 

 **Constraints:** 

- 2 <= nums.length <= 104
- 1 <= nums[i] <= 104

## Solution

**Language:** Python  
**Runtime:** 11 ms (beats 68.75%)  
**Memory:** 21.2 MB (beats 7.92%)  
**Submitted:** 2026-10-09T11:51:56.301Z  

```py
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n=len(nums)
        s=set()
        d=0
        m=0
        for i in nums:
            if i in s:
                d=i
            s.add(i)
        for i in range(1,n+1):
            if i not in s:
                m=i
                break

        return [d,m]
```

---

[View on LeetCode](https://leetcode.com/problems/set-mismatch/)