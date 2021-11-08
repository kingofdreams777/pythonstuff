"""
A phrase is a palindrome if, after converting all uppercase into lowercase letters and
removing all non-alphanumeric characters, it reads the same forward and backwars.
Alphanumeric characters include letters and numbers

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome

Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome

Constraints:
    1 <= len(s) <= 2 * 10^5
    s consists only of printable ascii characters
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum()).lower()
        if len(s) == 0:
            return True


        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True




solution = Solution()

s = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(s))
s = "race a car"
print(solution.isPalindrome(s))



