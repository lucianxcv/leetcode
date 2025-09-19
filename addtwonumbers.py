# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # Initialize a dummy node to simplify result handling
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0
    
    # Iterate over both linked lists
    while l1 or l2 or carry:
        # Get the values of the current nodes, or 0 if the node is None
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Calculate the sum of the two digits plus any carry
        total = val1 + val2 + carry
        carry = total // 10  # Calculate the new carry
        current.next = ListNode(total % 10)  # Create a new node with the result
        current = current.next  # Move the current pointer to the new node
        
        # Move to the next nodes in l1 and l2, if they exist
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    return dummy_head.next
