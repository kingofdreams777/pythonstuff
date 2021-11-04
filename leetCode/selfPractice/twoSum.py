"""
Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such
that they add up to target. 

You may assume that each input would have exactly one solution, and you may not use the same
element twice.

You can return the answer in any order

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
        Output explanation: Because nums [0] + nums [1] == 9, we return [0,1]

Example 2:
    Input: nums = [3,2,4], target = 6
    Ouput: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

Constraints:
    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
"""

class Solution:
    def twoSum(self, nums, target):
        prevMap = {} #value: index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            else:
                prevMap[n] = i

nums = [2,7,11,15]
target = 9
s = Solution()
print(s.twoSum(nums,target))

"""
Explanation: This solution keeps track of the difference between the current number and the target within the hash map prevMap.
The reason this works is because if the difference has already been detected then we have found the solution.

Enumerate seems to be a powerful class operator, allowing for tracking both the current index but also the current index value
With this problem, it asks to return the two indices of the two numbers that add up to the sum.
"""
