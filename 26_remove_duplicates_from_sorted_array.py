"""Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:
The judge will test your solution with the following code:"""

#Time Complexity: O(n)
#Space Complexity: O(1)

""" nums =  doesn't replace elements in the original list.
nums[:] = replaces element in place

In short, without [:], we're creating a new list object, which is against what this problem is asking for:
"Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory."
"""

from typing import List 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)

nums_ = [1,1,2]
checker = Solution()
checker.removeDuplicates(nums_)


def removeDuplicates2(nums: List[int]) -> int:
    counter_ = 0
    pointer = 0
    for i in range(len(nums)-1):
        print(i, counter_, pointer)
        if nums[pointer] == nums[pointer+1]:
            nums.pop(pointer)
            counter_ += 1
        else:
            pointer += 1
    return nums

removeDuplicates2([1,1,2])