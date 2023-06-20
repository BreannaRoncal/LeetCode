"""
Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example:
  Input: s = ["h","e","l","l","o"]
  Output: ["o","l","l","e","h"]
"""

def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    l_ptr = 0
    r_ptr = len(s) - 1
    while l_ptr < r_ptr:
        s[l_ptr], s[r_ptr] = s[r_ptr], s[l_ptr]
        l_ptr += 1
        r_ptr -= 1
        
