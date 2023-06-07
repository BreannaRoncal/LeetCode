"""
Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique 
element appears only once. The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # If nums is empty, then return 0
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        # Track the unique elements
        i = 0
        # Scan the array
        j = 1
        while j < nums_len:
            # If we find a unique element, we replace the duplicate with the new unique element
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            j += 1
        # Return the count of unique elements
        return i + 1
        
