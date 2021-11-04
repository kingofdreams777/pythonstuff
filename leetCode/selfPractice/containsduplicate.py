"""
Given an integer array nums, return true if any value appears at least twice
in the array and return false if every element is distinct

Example 1:
    Input: nums = [1,2,3,1]
    Output: true

Example 2:
    Input: nums = [1,2,3,4]
    Output: false

Example 3:
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

Constraints:
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
"""

class Solution:
    def containsDuplicate(self, nums) -> bool:
        d = {} # initialize hash map to keep track of count and characters in list
        
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        for key in d:
            if d[key] > 1:
                return True

        return False


s = Solution()
ex1 = [1,2,3,1]
ex2 = [1,2,3,4]
ex3 = [1,1,1,3,3,4,3,2,4,2]
ex4 = [2,14,18,22,22]

print(s.containsDuplicate(ex1))
print(s.containsDuplicate(ex2))
print(s.containsDuplicate(ex3))
print(s.containsDuplicate(ex4))



"""
Result: Submission accepted after placing return False statement outside of for key in d loop
    2nd try
Explanation: The reason this code works is because it creates a hash map the keeps track of
    each unique value within the array. If any of the values occur more than once,
    the value of that key in incremented within the hashmap. Needed to place the return False
    statement outside of the for loop otherwise it would only return True for the first key:value
    pair that was present within the hashmap.

Difficulty: Easy
"""




