"""
Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Example:
  Input: digits = [4,3,2,1]
  Output: [4,3,2,2]
  Explanation: The array represents the integer 4321.
  Incrementing by one gives 4321 + 1 = 4322.
  Thus, the result should be [4,3,2,2].
  
Example:
  Input: digits = [9]
  Output: [1,0]
  Explanation: The array represents the integer 9.
  Incrementing by one gives 9 + 1 = 10.
  Thus, the result should be [1,0].
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_num = ""
        for i in digits:
            str_num += str(i)
        int_num = int(str_num)
        int_num += 1
        str_num = str(int_num)

        new_digits = []
        for i in str_num:
            new_digits.append(int(i))
        return new_digits
