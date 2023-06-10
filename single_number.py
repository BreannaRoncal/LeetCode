"""
Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example:
  Input: nums = [4,1,2,1,2]
  Output: 4
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        found_single = 0
        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            print("i: " + str(nums[i]) + " i + 1: " + str(nums[i + 1]))
            if nums[i] != nums[i + 1]:
    
                found_single = nums[i]
                return found_single
        
            else:
                i += 1
        if len(nums) % 2 == 1 and found_single == 0:
            found_single = nums[-1]
        return found_single
        
