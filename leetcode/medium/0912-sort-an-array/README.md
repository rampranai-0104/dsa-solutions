# Sort an Array

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of integers `nums`, sort the array in ascending order and return it.

You must solve the problem  **without using any built-in**  functions in `O(nlog(n))` time complexity and with the smallest space complexity possible.

 

 **Example 1:** 

```
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

```

 **Example 2:** 

```
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessarily unique.

```

 

 **Constraints:** 

- 1 <= nums.length <= 5 * 104
- -5  *104 <= nums[i] <= 5*  104

## Solution

**Language:** Python  
**Runtime:** 803 ms (beats 20.96%)  
**Memory:** 38.2 MB (beats 5.59%)  
**Submitted:** 2026-10-01T06:21:11.489Z  

```py
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n=len(nums)
        t=[0]*n
        def merge(a,l,m,h):
            i=l
            j=m+1
            k=l
            while i<=m and j<=h:
                if a[i]<=a[j]:
                    t[k]=a[i]
                    i+=1
                else:
                    t[k]=a[j]
                    j+=1
                k+=1
            while i<=m:
                t[k]=a[i]
                i+=1
                k+=1
            while j<=h:
                t[k]=a[j]
                j+=1
                k+=1
            k=l
            while k<=h:
                a[k]=t[k]
                k+=1
        def mergesort(a,l,h):
            if l>=h:
                return 
            m=(l+h)//2
            mergesort(a,l,m)
            mergesort(a,m+1,h)
            merge(a,l,m,h)
        mergesort(nums,0,n-1)
        return nums
```

---

[View on LeetCode](https://leetcode.com/problems/sort-an-array/)