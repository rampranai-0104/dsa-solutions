# Longest Substring Without Repeating Characters

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `s`, find the length of the  **longest**   **substring**  without duplicate characters.

 

 **Example 1:** 

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

```

 **Example 2:** 

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

```

 **Example 3:** 

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

```

 

 **Constraints:** 

- 0 <= s.length <= 105
- s consists of English letters, digits, symbols and spaces.

## Solution

**Language:** Python  
**Runtime:** 246 ms (beats 29.08%)  
**Memory:** 20 MB (beats 12.37%)  
**Submitted:** 2026-10-14T15:22:00.817Z  

```py
class Solution:
    def lengthOfLongestSubstring(self, a: str) -> int:
        n=len(a)
        seen=set()
        i=0
        j=0
        m=0
        while j<n and i<n:
            if a[j] not in seen:
                seen.add(a[j])
                j+=1
                m=max(m,j-i)
            else:
                seen.remove(a[i])
                i+=1
        return m

```

---

[View on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)