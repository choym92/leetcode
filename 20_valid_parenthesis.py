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

"""
Idea:
We need to make sure we have open parenthesis first. 
Cannot start with the closed parenthesis. 
The ordering needs to be applied.
We will be removing top and the beginning of the list.
Therefore, we know that we need to utilize STACK
Create a hashmap. 

O(n) because we are having to go through the input character once. 
O(n) of memory because we are using a stack and the stack can be the size of the input. 
"""
class Solution:
    def isValid(self, s: str) -> bool:
        # hashmap and stack
        hashmap = {')':'(', ']':'[', '}':'{'}
        stack = []

        # go through each character at once of the string and 
        for char_ in s:
        # if the char is open paren add to the stack
            if char_ not in ']})': 
                stack.append(char_)
            elif stack: # if closed paren and in value in stack there is char in stack
                # pop and see if the value matches the according hashmap
                x = stack.pop()
                # if the ordering is off, return False
                if x != hashmap[char_]:
                    return False
            # if ordering is 
            else:
                return False
        # we check if the stack is empty else return False because it means the string contains closed parenthesis
        return True if len(stack) == 0 else False 

checker = Solution()

input1 = "()"
input2 = "()[]{}"
input3 = "(]"

checker.isValid(input1)
checker.isValid(input2)
checker.isValid(input3)
