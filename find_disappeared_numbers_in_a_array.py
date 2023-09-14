"""
Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 
Example 1:
  Input: nums = [4,3,2,7,8,2,3,1]
  Output: [5,6]

Example 2:
  Input: nums = [1,1]
  Output: [2]

 
Constraints:
  - n == nums.length
  - 1 <= n <= 105
  - 1 <= nums[i] <= n

The solution is:
  Time Complexity: O(n)
    It only iterates through the array once
    
  Space Complexity: O(1)
    It uses the given array to keep track of which numbers have been seen already

"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        disappeared_nums = []
        
        # Iterate through the array and use the given array to mark 
        # the number as negative meaning that we have already seen
        # it in the array
        for i in range(len(nums)):
            get_idx = abs(nums[i]) - 1
            if nums[get_idx] > 0:
                nums[get_idx] *= -1
                
        # Iterate through the array to see which numbers are positive,
        # meaning that the index it is at + 1 is missing from the array 
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                disappeared_nums.append(i)
                
        return disappeared_nums
