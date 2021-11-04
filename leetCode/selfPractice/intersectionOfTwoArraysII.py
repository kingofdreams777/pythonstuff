"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element
in the result must appear as many times as it shows in both arrays and you may return the result
in any order

Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2,2]

Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [4,9]

Constraints:
    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 1000
"""

class Solution:
    def intersect(self, nums1, nums2):
        lArray = []
        if len(nums1) <= len(nums2):
            sList = nums1
            lList = nums2
        else:
            sList = nums2
            lList = nums1

        for i in range(len(sList) - 1):
            for j in range(len(lList) - 1):
                if sList[i] == lList[j]:
                    lArray.append(sList.pop(i))

        return lArray

s = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
s.intersect(nums1,nums2)
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
s.intersect(nums1,nums2)

