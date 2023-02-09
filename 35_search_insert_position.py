class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
        You must write an algorithm with O(log n) runtime complexity.

        My Solution
        """
        i = 0 
        while i < len(nums):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                i+=1
            else: 
                return i
        return i


checker = Solution()
checker.searchInsert([1,2,3,5], 5)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Binary search way O(log n)
        """
        i = 0
        j = len(nums) - 1
        while(i <= j):
            pivot = (i + j) // 2
            if (nums[pivot] == target):
                return pivot
            elif (nums[pivot] > target):
                j = pivot - 1
            else:
                i = pivot + 1
        return i


checker = Solution()
checker.searchInsert([1,2,3,5], 5)