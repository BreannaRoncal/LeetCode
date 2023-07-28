"""
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
  - Open brackets must be closed by the same type of brackets.
  - Open brackets must be closed in the correct order.
  - Every close bracket has a corresponding open bracket of the same type.
   

Example 1:
  Input: s = "()"
  Output: true
  
Example 2:
  Input: s = "()[]{}"
  Output: true
  
Example 3:
  Input: s = "(]"
  Output: false
 

Constraints:
  - 1 <= s.length <= 104
  - s consists of parentheses only '()[]{}'.
"""

from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        open_pars = ['(', '[', '{']
        close_pars = [')', ']', '}']
        
        str_stack = deque()
        for i in s:
            if i in open_pars:
                str_stack.append(i)
            elif i in close_pars:
                idx = close_pars.index(i)
                if len(str_stack) > 0 and open_pars[idx] == str_stack[-1]:
                    str_stack.pop()
                else:
                    return False
                
        return True if len(str_stack) == 0 else False
           
