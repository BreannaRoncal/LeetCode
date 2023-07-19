"""
Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 
Example 1:
  Input: n = 2
  Output: 2
  Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
    
Example 2:
  Input: n = 3
  Output: 3
  Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
 

Constraints:
  - 1 <= n <= 45
"""

class Solution:
    def createDPTable(self, n):
        # Create fibonacci table for dynamic programming
        # This is faster than calling the fibonacci method everytime
        dp_table = [0 for i in range(n)]
        dp_table[0] = 1
        dp_table[1] = 1
        
        for i in range(2, n):
            j = 1
            while j <= 2 and j <= i:
                dp_table[i] = dp_table[i] + dp_table[i - j]
                j += 1
        return dp_table[n - 1]
            
    def climbStairs(self, n: int) -> int:
        # Add one to fib because 1 is the minimum stair to climb a staircase of 1
        return self.createDPTable(n + 1)
        
