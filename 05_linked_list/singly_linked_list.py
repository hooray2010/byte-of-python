"""
单链表反转（递归）
两个有序的链表合并（利用中间节点，指针依次后移）

链表中环的检测
删除链表倒数第n个结点
求链表的中间结点
"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.__data = data
        self.__next = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next_node(self):
        return self.__next

    @next_node.setter
    def next_node(self, next_node):
        self.__next = next_node
        return next_node


class SinglyLinkedList(object):
    """
    引用哨兵节点，带头链表
    """

    def __init__(self):
        self.__head = Node()

    def create_node(self, value):
        return Node(value)

    def insert_to_head(self, value):
        node = Node(value)
        """
        须先设置 next 节点，否则指针丢失，导致内存泄漏
        修改 2 个指针，分别为 next_node（改为head） 与 head（改为node）
        """
        node.next_node = self.__head.next_node
        self.__head.next_node = node

    def insert_to_end(self, end_node):
        current_node = self.__head
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = end_node

    def insert_after(self, node, value):
        if node is None:
            return
        new_node = Node(value)
        """
        先链接 新节点 与 新节点之后的节点，否则 后面节点 丢失引用
        """
        new_node.next_node = node.next_node
        node.next_node = new_node

    def insert_before(self, node, value):
        if node is None:
            return
        # 此时，在链表头插入节点，则直接插入
        if node == self.__head:
            self.insert_to_head(value)
            return

        # 从头开始找指定Node之前的pre_node，再复用代码
        pre_node = self.__head
        while pre_node.next_node != node:
            if pre_node.next_node is None:
                return
            else:
                pre_node = pre_node.next_node

        # 运行至此，则必定已找到pre_node
        self.insert_after(pre_node, value)

    def delete_by_node(self, node):
        # 若链表为空，则不处理
        if self.__head is None:
            return

        # 若删除的节点为头节点，则将指针head直接指向next_node
        if self.__head == node:
            self.__head = node.next_node
            return

        # 循环查找要删除的节点，之前的节点
        pre_node = self.__head
        while pre_node.next_node != node:
            if pre_node.next_node is None:
                return
            else:
                pre_node = pre_node.next_node

        # 运行至此，则必定已找到pre_node
        pre_node.next_node = node.next_node

    def delete_by_value(self, value):
        # 若链表为空，则不处理
        if self.__head is None:
            return

        # 若删除的节点为头节点，则将指针head直接指向next_node
        if self.__head.data == value:
            self.__head = self.__head.next_node
            return

        # 循环查找要删除的节点，之前的节点
        pre_node = self.__head
        while pre_node.next_node.data != value:
            if pre_node.next_node is None:
                return
            else:
                pre_node = pre_node.next_node

        # 运行至此，则必定已找到pre_node，只需将pre_node的next_node指针直接后移
        pre_node.next_node = pre_node.next_node.next_node

    def delete_last_n_node(self, n):
        """
        设置fast、slow两个指针，fast先走n步
        然后，fast、slow再同时走
        fast走到末尾时，slow指向倒数n个节点
        """
        fast = self.__head.next_node
        slow = self.__head.next_node
        step = 1

        while step < n:
            fast = fast.next_node
            step += 1

        while fast.next_node is not None:
            # 保存slow之前的节点，作删除需要用
            pre_node = slow
            fast = fast.next_node
            slow = slow.next_node

        # fast走到末尾，此时 pre_node.next_node = slow
        pre_node.next_node = slow.next_node

    def find_by_value(self, value):
        node = self.__head
        while (node is not None) and (node.data != value):
            node = node.next_node
        return node

    def find_by_index(self, index):
        node = self.__head
        pos = 0
        # index 超出，则返回最后一个节点
        while (node is not None) and (pos != index):
            node = node.next_node
            pos += 1
        return node

    def find_mid_node(self):
        if (self.__head is None) or (self.__head.next_node is None):
            return None

        fast = self.__head
        slow = self.__head

        while fast.next_node is not None:
            fast = fast.next_node.next_node
            slow = slow.next_node
        return slow

    def reverse_all(self):
        if self.__head is None or self.__head.next_node is None:
            return

        self.__reverse_one_node(self.__head.next_node)

    def __reverse_one_node(self, current_node):
        """
        https://www.bilibili.com/video/BV1Cz411B7qd?p=57

        递归：
        head - 4 - None
        head - 4 -3 - None
        """
        if current_node.next_node is None:
            self.__head.next_node = current_node
            return current_node

        pre_node = self.__reverse_one_node(current_node.next_node)

        pre_node.next_node = current_node
        current_node.next_node = None

        return current_node

    def has_ring(self):
        fast = self.__head
        slow = self.__head

        while (fast is not None) and (fast.next_node is not None):
            fast = fast.next_node.next_node
            slow = slow.next_node
            if fast == slow:
                return True

    def print_all(self):
        if self.has_ring():
            print("当前链表包含环，无法打印！")
            return

        current_node = self.__head

        if current_node is None:
            print("当前链表还没有数据")
            return

        while current_node.next_node is not None:
            print(str(current_node.data) + ">", end="")
            current_node = current_node.next_node
        # 打印最后一个节点
        print(str(current_node.data))


def merge_sorted_list(node1: Node, node2: Node):
    """
    利用中间节点，指针后移
    """
    head = Node()
    tail = head
    while (node1 is not None) and (node2 is not None):
        if node1.data <= node2.data:
            tail.next_node = node1
            node1 = node1.next_node
        else:
            tail.next_node = node2
            node2 = node2.next_node
        tail = tail.next_node

    while (node1 is not None):
        tail.next_node = node1
        node1 = node1.next_node
        tail = tail.next_node

    while (node2 is not None):
        tail.next_node = node2
        node2 = node2.next_node
        tail = tail.next_node

    return head.next_node


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    node1.next_node = node3
    node3.next_node = node5

    node2.next_node = node4
    node4.next_node = node6

    merge_node = merge_sorted_list(node1, node2)

    ll_merge = SinglyLinkedList()
    ll_merge.insert_to_end(merge_node)
    print("合并后的链表为：")
    ll_merge.print_all()

    ll = SinglyLinkedList()
    ll.print_all()

    ll.insert_to_head(0)
    ll.print_all()

    node_0 = ll.find_by_index(0)
    ll.insert_after(node_0, 1)
    ll.print_all()

    node_1 = ll.find_by_value(1)
    ll.insert_after(node_1, 2)
    ll.print_all()

    ll.reverse_all()
    print("翻转后的结果为：")
    ll.print_all()

    ll.insert_to_head(6)
    ll.insert_to_head(7)
    ll.insert_to_head(8)
    ll.print_all()

    last_n = 5
    ll.delete_last_n_node(last_n)
    print("删除倒数第" + last_n.__str__() + "个节点：")
    ll.print_all()

    ll.reverse_all()
    print("翻转后的结果为：")
    ll.print_all()

    # 加环
    node_2 = ll.find_by_value(2)
    node_2.next_node = node_0
    ll.print_all()
    print("该单链表是否有环：" + ll.has_ring().__str__())
