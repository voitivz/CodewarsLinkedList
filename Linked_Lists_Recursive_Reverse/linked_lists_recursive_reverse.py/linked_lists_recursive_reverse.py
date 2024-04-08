class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    if head is None or head.next is None:
        return head
    reversed_head = reverse(head.next)

    head.next.next = head
    head.next = None
    
    return reversed_head