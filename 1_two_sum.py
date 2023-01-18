# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

 
"""
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        return indices of two numbers that adds up to a target with list of integers        
        """

        seen = {}

        for counter_, int_ in enumerate(nums):
            remainder_ = target - int_
            
            if remainder_ in seen:
                return [seen[remainder_], counter_]
            else:
                seen[int_] = counter_
            print(seen)

checker = Solution()

print(checker.twoSum([3,2,4], 6))
print(checker.twoSum([2,7,11,15], 26))

# Iterating and inserting elements into the hash table, we also look back and check if current lement's complement 
# already exists in the hash table. Time complexity: O(n). Space complexity: O(n). The 