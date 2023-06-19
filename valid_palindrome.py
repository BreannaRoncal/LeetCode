"""
Valid Palindrom

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example:
  Input: s = "A man, a plan, a canal: Panama"
  Output: true
  Explanation: "amanaplanacanalpanama" is a palindrome.
  
  Input: s = "0P"
  Output: false
  Explanation: "0P" does not equal "P0"
  
"""

def isPalindrome(self, s: str) -> bool:
  only_alpha = "".join(filter(lambda x: x.isalnum() == True, s)).lower()
  print(only_alpha)
  print(only_alpha[::-1])
  return only_alpha == only_alpha[::-1]
