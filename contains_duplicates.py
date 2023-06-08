"""
Contains Duplicates

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Solution that uses less memory by sorting the list first:

    class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        print(nums)
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
        
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup_dict = {}
        if len(nums) == 0 or len(nums) == 1:
            return False
        else:
            for i in nums:
                print(i)
                if i in dup_dict:
                    return True
                if i not in dup_dict:
                    dup_dict[i] = 0
            return False
        
