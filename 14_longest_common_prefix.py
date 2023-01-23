# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

"""
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for char_ in zip(*strs):
            if len(set(char_)) == 1:
                result += char_[0]
            else:
                return result
        return result


strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]

checker = Solution()
checker.longestCommonPrefix(strs1)
checker.longestCommonPrefix(strs2)

# Intuition:
# compare each letter of strings and if match, add to an empty string until you hit a character that doesn't match
# return the string added so far
