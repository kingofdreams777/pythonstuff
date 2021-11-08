"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: True

Example 2:
    Input: s = "rat", t = "car"
    Output: False

Constraints:
    1 <= len(s), len(t) <= 5 * 10^4
    s and t consist of lowercase english letters
"""

class Solution:
    def isAnagram(self,s: str,t: str):
        s = s.replace(' ','')
        t = t.replace(' ', '')

        if len(s) != len(t):
            return False

        count = {}

        for l in s:
            if l in count:
                count[l] += 1
            else:
                count[l] = 1

        for l in t:
            if l in count:
                count[l] -= 1
            else:
                count[l] = 1

        for k in count:
            if count[k] != 0:
                return False

        return True
