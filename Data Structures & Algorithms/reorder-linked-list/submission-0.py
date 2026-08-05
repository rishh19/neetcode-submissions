# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #middle

        s=head
        f=head

        while f and f.next:
            s=s.next
            f=f.next.next

        #split
        second=s.next
        s.next=None

        #reverse second half

        prev=None
        curr=second

        while curr:
            nxtnode = curr.next
            curr.next=prev
            prev=curr
            curr=nxtnode

        second=prev

        #merge alterrnate

        first=head
        while second:
            temp1=first.next
            temp2=second.next

            first.next=second
            second.next=temp1
            first=temp1
            second=temp2

