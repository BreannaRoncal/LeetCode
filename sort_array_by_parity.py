"""
Sort Array by Parity

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

 

Example 1:
  Input: nums = [3,1,2,4]
  Output: [2,4,3,1]
  Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:
  Input: nums = [0]
  Output: [0]

 
Constraints:
  - 1 <= nums.length <= 5000
  - 0 <= nums[i] <= 5000

Time Complexity: O(n) because it is using two-pointers
Space Complexity: O(1) because it is in-place
"""

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        # Pointer at the beginning of the list
        i = 0
        
        # Pointer at the end of the list
        j = len(nums) - 1
        
        # Loop through til the pointers meet in the middle
        while i < j:
            # If parity of nums[i] is greater than parity of nums[j]
            # then that mean nums[i] is an odd number and nums[j] is an even number
            if nums[i] % 2 > nums[j] % 2:
                
                # Swap so they are in the correct spot
                nums[i], nums[j] = nums[j], nums[i]
            
            # If nums[i] is an even number, then increment pointer
            if nums[i] % 2 == 0:
                i += 1
                
            # If nums[j] is an odd number, then decrement pointer
            if nums[j] % 2 == 1:
                j -= 1
        
        return nums
