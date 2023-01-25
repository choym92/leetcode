# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
"""
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""

class Solution:
    def isValid(self, s: str) -> bool:
        paren_dict = {')':'(', ']':'[', '}':'{'}
        stack = []
        for char_ in s:
            if char_ not in ']})':
                stack.append(char_)
            elif stack:
                x = stack.pop()
                if x != paren_dict[char_]:
                    return False
            else:
                return False
        return True if len(stack) == 0 else False 

checker = Solution()

input1 = "()"
input2 = "()[]{}"
input3 = "(]"

checker.isValid(input1)
checker.isValid(input2)
checker.isValid(input3)
