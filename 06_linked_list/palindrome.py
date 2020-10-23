"""
判断是否是回文
1、利用快慢指针，找到中点节点slow
2、反转中间节点slow之后的链表
3、遍历原始头节点head与新链表slow
"""
import sys

sys.path.append('singly_linked_list')
from singly_linked_list import SinglyLinkedList


def is_palindrome(ll: SinglyLinkedList):
    ll.print_all()

    fast = ll.head
    slow = ll.head

    pos = 0
    while fast and fast.next_node:
        fast = fast.next_node.next_node
        slow = slow.next_node
        pos += 1

    ll2 = SinglyLinkedList()
    ll2.head.next_node = slow
    ll2.reverse_all2()

    origin_head = ll.head.next_node
    reverse_head = ll2.head.next_node
    is_pal = True
    while origin_head and reverse_head:
        if origin_head.data == reverse_head.data:
            origin_head = origin_head.next_node
            reverse_head = reverse_head.next_node
        else:
            is_pal = False
            break
    return is_pal


if __name__ == '__main__':
    # the result should be False, True, True, True, True
    test_str_arr = ['abcdabc', 'aa', 'aba', 'abba', 'abcba']
    for str in test_str_arr:
        ll = SinglyLinkedList()
        for s in str:
            ll.insert_to_head(s)
        print(is_palindrome(ll))
