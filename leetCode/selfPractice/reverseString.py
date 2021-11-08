"""
Write a function that reverses a string. The input string is given as an array of characters s

Example 1:
    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","he"]

Constraints:
    1 <= len(s) <= 10^5
    s[i] is a printable ascii character

Follow up: Do not allocate extra space for another array. You must do this by modifying the
input array in-place with O(1) extra memory
"""

class Solution:
    def reverseString(self, s):
        start = 0
        end = len(s) - 1

        while start < end:
            intermediate = s[end]
            s[end] = s[start]
            s[start] = intermediate
            start += 1
            end -= 1
        print(s)


s = Solution()
string = ["h","e","l","l","o"]
s.reverseString(string)

"""
Explanation: Learned this algorithm while teaching myself C++ on Udemy. Pretty straightforward.
Increment the start value and decrement the end value and make an intermediary value to assign
start to before the replacement occurs.

Very easy imo
"""
