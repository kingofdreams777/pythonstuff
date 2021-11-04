"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that
single one. You must implement a solution with a linear runtime complexity and use only constant
extra space

Example 1:
    Input: nums = [2,2,1]
    Output: 1

Example 2:
    Input: nums = [4,1,2,1,2]
    Output: 4

Example 3:
    Input: nums = [1]
    Output: 1

Constraints:
    1 <= nums.length <= 3 * 10^4
    -3 * 10^3 <= nums[i] <= 3 * 10^4
    Each element in the array appears twice except for one element which appears only once
"""

class Solution:
    def singleNumber(self, nums) -> int:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        for key in d:
            if d[key] == 1:
                return key

        return None
            

s = Solution()

nums = [2,2,1]
print(s.singleNumber(nums))
nums = [4,1,2,1,2]
print(s.singleNumber(nums))
nums = [1]
print(s.singleNumber(nums))

"""
Another hashmap and array problem. Same solution here. Hashmap that keeps track of the count of
elements within the array. Return the solution that only has the count of 1 within the array.
Super straight forward

Difficult: Very Easy
"""
