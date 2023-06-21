"""
First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
  Input: s = "leetcode"
  Output: 0
  
Example 2:
  Input: s = "loveleetcode"
  Output: 2
  
Example 3:
  Input: s = "aabb"
  Output: -1
  
"""

from collections import Counter

def firstUniqChar(self, s: str) -> int:
  # Create a counter object, a dictionary that counts the frequency of each character
  count_s = Counter(s)
  
  # Enumerate through s and find the first character to appear once and return its index
  for key, val in enumerate(s):
      if count_s[val] == 1:
          return key
  return -1
