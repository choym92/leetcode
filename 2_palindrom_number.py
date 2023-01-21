# Given an integer x, return true if x is a 
# palindrome , and false otherwise.

"""
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""

# Follow up: Could you solve it without converting the integer to a string?

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        isPalindrome_ = str(x) == str(x)[::-1]
        return isPalindrome_
    
    def followUpPal(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0): # checking if x is negative number or if x is possitive but end in 0
            return False
        
        result = 0
        while x > result:
            result = result * 10 + x % 10
            x = x//10
        
        return True if (x == result or x == result//10) else False

checker = Solution()

print(checker.isPalindrome(121))
print(checker.isPalindrome(322423))

print(checker.followUpPal(121))
print(checker.followUpPal(10))
print(checker.followUpPal(1212))
