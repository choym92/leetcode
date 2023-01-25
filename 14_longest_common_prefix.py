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

"""
Method:
simutenously iterate through all of the strings that were given.
One of the string can be shorter than the other.
Iterating through every single characters where 

O(n) and n being the number of characters.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # initialize initial result string
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


# Checking zip and *zip
for i in zip([1,2,3],[4,5,6]):
    print(i)
# (1, 4)
# (2, 5)
# (3, 6)
# take one char or value from each element treating them as if they are a list of on its own
for i in zip(*['abc', '111', '222']):
    print(i)

# ('a', '1', '2')
# ('b', '1', '2')
# ('c', '1', '2')

for i in zip(['abc', '111', '222']):
    print(i)
# ('abc',)
# ('111',)
# ('222',)