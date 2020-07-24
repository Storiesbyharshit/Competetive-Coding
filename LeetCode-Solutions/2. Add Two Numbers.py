class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        carry = 0
        curr = ListNode (0)
        result = curr
        
        
        while l1 or l2 or carry :
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
                
            curr.next = ListNode(carry%10)
            curr = curr.next
            carry //= 10
        return result.next
