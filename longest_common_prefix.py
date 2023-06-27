"""
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
  Input: strs = ["flower","flow","flight"]
  Output: "fl"
  
Example 2:
  Input: strs = ["dog","racecar","car"]
  Output: ""
  Explanation: There is no common prefix among the input strings.
 
Constraints:
  - 1 <= strs.length <= 200
  - 0 <= strs[i].length <= 200
  - strs[i] consists of only lowercase English letters.
  
"""

def longestCommonPrefix(self, strs: List[str]) -> str:
    lcp = ""
    
    # find the len of the smallest str because this will be the max lcp
    smallest_str = len(strs[0])
    for s in range(len(strs)):
        smallest_str = min(smallest_str, len(strs[s]))
    
    # keep track of the current character to compare to each of the words in strs
    for i in range(smallest_str):
        curr_char = strs[0][i]
        for j in range(len(strs)):
            if strs[j][i] != curr_char:
                return lcp
        lcp += curr_char
    return lcp
