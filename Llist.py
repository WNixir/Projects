class Node:
    '''
    A node for a linked list
    '''

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


def sum(head):
    '''(linkedlist, NoneType) -> int
    takes in the head of a linked list, whose data values are all ints
    function returns the sum of all integers

    REQ: all data must be ints
    '''
    cur = head
    _sum = 0
    # if the list is empty
    # return 0
    if head is None:
        _sum = 0
    else:
        # loop over all the nodes and add each value to sum
        while cur.next_node is not None:
            _sum += cur.data
            cur = cur.next_node
        # add the data at the last node to the sum
        _sum += cur.data
    return _sum


def reverse(head):
    '''(linkedlist) -> linkedlist
    takes in the head of a linked list, return the head of
    reversed linked list
    '''
    # keep track of the current node and the previous node
    prev = None
    cur = head
    # loop over the list and change the pointers to reverse the list
    while cur is not None:
        # save the next node before getting rid of the cur pointer to it
        next = cur.next_node
        # make cur point to prev which was None
        cur.next_node = prev
        prev = cur
        cur = next
    head = prev
    return head


def splice(head, index):
    '''(linkedlist, int) -> linkedlist
    takes in the head and an index of linked list, return the head of a
    spliced linked list, where the values before the index and the values
    after the index are swapped

    i.e. a = head -> A -> B -> C -> D -> E -> F -> None
    >>> splice(a, 3)
    head -> E -> F -> D -> A -> B -> C -> None
    '''
    ret_head = None
    # return the head if the linked list is empty
    # or if there is only 1 element in the list
    if (head is None) or (head.next_node is None):
        ret_head = head

    index_node = head
    prev = head
    end = head
    length = 0
    index_num = 0
    # loop over the list to find the last node
    while end.next_node is not None:
        end = end.next_node
        length += 1

    # if the index is 0
    if index == 0:
        end.next_node = index_node
        ret_head = index_node.next_node
        index_node.next_node = None

    else:
        # find the index node
        while index_num < index:
            prev = index_node
            index_node = index_node.next_node
            ret_head = index_node.next_node
            index_num += 1
            # if the index node is the last node
        if length == index:
            end.next_node = head
            ret_head = end
            prev.next_node = None
        else:
            # point the last node to the index node
            end.next_node = index_node
            # the index node point to the current head
            index_node.next_node = head
            # the node before the index node point to None
            prev.next_node = None
    return ret_head
