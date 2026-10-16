# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of integers `arr` and two integers `k` and `threshold`, return  *the number of sub-arrays of size* `k` *and average greater than or equal to* `threshold`.

 

 **Example 1:** 

```
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

```

 **Example 2:** 

```
Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.

```

 

 **Constraints:** 

- 1 <= arr.length <= 105
- 1 <= arr[i] <= 104
- 1 <= k <= arr.length
- 0 <= threshold <= 104

## Solution

**Language:** Python  
**Runtime:** 39 ms (beats 81.37%)  
**Memory:** 30.8 MB (beats 17.47%)  
**Submitted:** 2026-10-16T15:33:26.289Z  

```py
class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, t: int) -> int:
        n=len(arr)
        c=0
        """for i in range(n-k+1):
            s=sum(arr[i:i+k]) 
            if s>=k*t:
                c+=1"""
        s=sum(arr[:k])
        if s>=k*t:
            c+=1
        for i in range(n-k):
            s-=arr[i]
            s+=arr[i+k]
            if s>=k*t:
                c+=1
        return c
```

---

[View on LeetCode](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)