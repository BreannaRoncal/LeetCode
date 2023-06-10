"""
Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter_array = []
        nums2_copy = nums2
        for i in range(len(nums1)):
            if nums1[i] in nums2_copy:
                inter_array.append(nums1[i])
                nums2_copy.remove(nums1[i])
        
        return inter_array
        
