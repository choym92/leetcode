# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.
"""
Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false

"""

# n = 2**x
# log(n) = x log(2)
# log(n) / log(2) = x
# if remainder division returns 0 then int else float


"""

Understanding Power of Two Checks in Python
When determining whether a number is a power of two, two efficient methods stand out: the bitwise method and the repeated division method. Each has its unique approach and efficiency, suitable for different scenarios.

Method 1: Bitwise Operations
Bitwise operations work directly with the binary representation of numbers. The '&' (AND) operator is particularly useful for this task, comparing each bit of its first operand to the corresponding bit of its second operand. If both bits are 1, the result is 1. Otherwise, the result is 0.

Example with n = 5:

The binary representation of 5 is 101.
The binary representation of 4 (5 - 1) is 100.
Comparing the bits from right to left:

The first bit: 1 (from 101) AND 0 (from 100) equals 0.
The second bit: 0 AND 0 equals 0.
The third bit: 1 AND 1 equals 1.
Thus, the bitwise AND result is 100 (binary), which is 4 in decimal.

Subtracting 1 from a Power of Two:

Subtracting 1 from a power of two flips all the bits following the highest 1 bit:

2 in binary: 10; 2 - 1 = 1 (01 in binary).
4 in binary: 100; 4 - 1 = 3 (011 in binary).
8 in binary: 1000; 8 - 1 = 7 (0111 in binary).
This behavior ensures that n & (n-1) returns 0 for powers of two, offering a quick and reliable check.

Efficiency: The bitwise method has a time complexity of O(1), making it incredibly efficient as it performs a constant number of operations regardless of the input size.

Method 2: Repeated Division
The repeated division method checks if a number is a power of two by continuously dividing the number by two until it either reaches 1 (confirming it is a power of two) or encounters an odd number (confirming it is not).

Efficiency:

The time complexity for the repeated division method is O(log n). This is because each division by two effectively halves the input size, akin to the operation of a binary search. Though not as instant as the bitwise approach, this method is still highly efficient, especially for large numbers.

In Summary:

Both methods offer clear insights into checking for powers of two, with the bitwise operation standing out for its elegance and speed, and the repeated division method providing a straightforward, iterative approach. Choosing between them depends on your specific needs and the context in which you're working.

"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:  # Edge case
            return False
        if n & (n - 1) == 0:
            return True

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 2 != 0:
                return False
            n //= 2
        return True

checker = Solution()

print(checker.isPowerOfTwo(536870912))
print(checker.isPowerOfTwo(1))
