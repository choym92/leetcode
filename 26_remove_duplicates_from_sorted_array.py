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

# Solution 1
class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)

# Solution 2
class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer_ = 0
        for i in range(len(nums)-1):
            if nums[pointer_] == nums[pointer_+1]:
                nums.pop(pointer_)
            else:
                pointer_ += 1
        return len(nums)

checker1 = Solution1()
checker2 = Solution2()

checker1.removeDuplicates([1,1,2,3,4,5,6,6])
checker2.removeDuplicates([1,1,2,3,4,5,6,6])