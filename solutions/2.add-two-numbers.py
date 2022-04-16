#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
from multiprocessing.sharedctypes import Value
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        l1_current_head, l2_current_head = l1, l2
        current_node = dummy_head
        carry_number = 0
        while l1_current_head is not None or l2_current_head is not None:
            l1_value, l2_value = 0, 0
            if l1_current_head is not None:
                l1_value = l1_current_head.val
            if l2_current_head is not None:
                l2_value = l2_current_head.val

            res = carry_number + l1_value + l2_value
            carry_number = res // 10
            current_node.next = ListNode(res % 10)
            current_node = current_node.next

            if l1_current_head is not None:
                l1_current_head = l1_current_head.next
            if l2_current_head is not None:
                l2_current_head = l2_current_head.next

        if carry_number > 0:
            current_node.next = ListNode(carry_number)
        return dummy_head.next
        # @lc code=end
