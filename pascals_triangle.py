"""
Pascals Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:



Example 1:
  Input: numRows = 5
  Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
  
Example 2:
  Input: numRows = 1
  Output: [[1]]
   

Constraints:
  - 1 <= numRows <= 30



Another Solution:
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals = []
        for i in range(numRows + 1):
            ith_row = []
            p = 1
            for j in range(1, i + 1):
                ith_row.append(p)
                p = p * (i - j) // j
            pascals.append(ith_row)
        return pascals[1:]
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals = [[1]]
        
        for i in range(numRows - 1):
            temp = [0] + pascals[-1] + [0]
            new_row = []
            for j in range(len(pascals[-1]) + 1):
                new_row.append(temp[j] + temp[j + 1])
            pascals.append(new_row)
        return pascals
        
