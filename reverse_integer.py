"""
Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
  Input: x = 123
  Output: 321

Example 2:
  Input: x = -123
  Output: -321

Example 3:
  Input: x = 120
  Output: 21
  
  
  
  
~~~~~~~~~~~~~~~~~~ Another Solution ~~~~~~~~~~~~~~~~~~
def reverse(self, x: int) -> int:
        y = str(abs(x))
        y = y.strip()
        y = y[::-1]
        output = int(y)
        if output >= 2** 31 -1 or output <= -2** 31:
            return 0
        elif x < 0:
            return -1 * output
        else:
            return output
"""

def reverse(self, x: int) -> int:
        x_str = str(x)
        x_str_rev = ''
        if x < 0:
            x_str = x_str[1:]
            x_str_rev = x_str[::-1]
            x_rev = int(x_str_rev) * -1
        else:
            x_str_rev = x_str[::-1]
            x_rev = int(x_str_rev) 
        if x_rev < -pow(2, 31) or x_rev > pow(2, 31) - 1:
            return 0
        return x_rev
            
        
