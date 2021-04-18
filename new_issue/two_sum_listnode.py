class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1.val == 0 and l1.next is None:
        return l2
    if l2.val == 0 and l2.next is None:
        return l1

    ret = ListNode((l1.val+l2.val)%10)
    last = ret
    advance = l1.val+l2.val >= 10
    l1 = l1.next
    l2 = l2.next
    while l1 is not None or l2 is not None:
        num1 = l1.val if l1 is not None else 0
        num2 = l2.val if l2 is not None else 0
        sum = num1 + num2
        if advance:
            sum += 1
        advance = sum >= 10
        new_node = ListNode(sum%10)
        last.next = new_node
        last = new_node
        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None
    if advance:
        last.next = ListNode(1)
    return ret

if __name__ == "__main__":
    l1 = [0]
    l2 = [5, 6, 4]
    test1 = ListNode(l1[0])
    last1 = test1
    test2 = ListNode(l2[0])
    last2 = test2
    for item in l1[1:]:
        new_node = ListNode(item)
        last1.next = new_node
        last1 = new_node
    for item in l2[1:]:
        new_node = ListNode(item)
        last2.next = new_node
        last2 = new_node
    ret = addTwoNumbers(test1,test2)
    while ret is not None:
        print ret.val
        ret = ret.next