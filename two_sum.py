"""
Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example:
  Input: nums = [2,7,11,15], target = 9
  Output: [0,1]
  Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret_idx = []
        # Create dictionary of nums values and their index
        nums_idx = {key: i for i, key in enumerate(nums)}
        
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in nums_idx:
                if i != nums_idx[remainder]:
                    ret_idx.append(i)
                    #print('i:', i)
                    ret_idx.append(nums_idx[remainder])
                    #print('nums_idx', nums_idx[remainder])
                    return ret_idx
                
        return ret_idx
