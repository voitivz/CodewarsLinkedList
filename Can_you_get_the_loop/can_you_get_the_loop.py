def loop_size(node):
    slow_ptr = node.next
    fast_ptr = node.next.next
    
    while slow_ptr != fast_ptr:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    
    slow_ptr = node
    
    while slow_ptr != fast_ptr:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next
    
    size = 1
    fast_ptr = fast_ptr.next
    while slow_ptr != fast_ptr:
        size += 1
        fast_ptr = fast_ptr.next
    
    return size