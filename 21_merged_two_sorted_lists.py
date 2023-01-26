
# Definition for singly-linked list.

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

"""
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""

# if one of the list is empty, just take the rest because they are both sorted
# the solution has linear time complexity where O(m+n) is total number of nodes in
# the input lists. Because it is merged list is appended from each one,
# also space is O(1)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# This function takes in the heads of two sorted linked lists (list1 and list2)
# as input. It creates a dummy node as the starting point for the merged list. 
# It then iterates through both input lists, comparing the values of the current 
# nodes in each list. The smaller value is added to the merged list and the 
# pointer for that list is moved to the next node. Once one of the input lists 
# is exhausted, the remaining nodes from the non-empty list are added to the 
# merged list. The head of the merged list is returned.

# linkedlist is about pointers and point to a memory location.
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        # create dummy 
        dummy = temp = ListNode()
        print(f'1. dummy: {dummy.val}')
        
        # if either of the lists is empty return the other
        if list1 is None: return list2
        if list2 is None: return list1

        # while both have values
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        # find none empty list and append 
        if list1:
            temp.next = list1
        elif list2:
            temp.next = list2
        
        return dummy.next       
