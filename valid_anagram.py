"""
Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
  Input: s = "anagram", t = "nagaram"
  Output: true
  
Example 2:
  Input: s = "rat", t = "car"
  Output: false
  
"""

from collections import Counter

def isAnagram(self, s: str, t: str) -> bool:
    # If s and t are different lengths, then they cannot be anagrams
    if len(s) != len(t):
        return False
    
    # Make a counter dictionary for the frequency of characters in both s and t
    s_counter = Counter(s)
    t_counter = Counter(t)
    
    # Compare the count of each character, and if they do not match, then they are not anagrams
    for key, val in enumerate(s):
        if s_counter[val] != t_counter[val]:
            return False
    return True
        
