# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur = head
        num = []
        while cur:
            num.append(cur.val)
            cur=cur.next
        i=0
        maxSum = 0
        while i <= len(num)/2:
            maxSum = max(maxSum, (num[i]+num[-1-i]))
            i+=1
        return maxSum
