class DbLinkedNode:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:
    """
    leet code: 146
        运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。
        它应该支持以下操作： 获取数据 get 和 写入数据 put 。
        获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
        写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。
            当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间

    哈希表+双向链表
    哈希表: 查询 O(1)
    双向链表: 有序, 增删操作 O(1)
    """

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hkeys = {}

        # 首尾2个哨兵节点，避免越界
        self.head = DbLinkedNode(None, -1)
        self.tail = DbLinkedNode(None, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def put(self, key: int, value: int) -> None:
        if key in self.hkeys.keys():
            # 删除命中的节点，再加入首部
            current_node = self.delete_node_by_key(key)
            self.insert_to_head(current_node)
        else:
            # 新节点加入哈希表
            new_node = DbLinkedNode(key, value)
            self.hkeys[key] = new_node

            self.insert_to_head(new_node)

            if len(self.hkeys.keys()) > self.cap:
                # 删除哈希表中，尾节点数据
                self.hkeys.pop(self.tail.prev.key)
                # 删除尾节点
                # self.tail.prev.prev.next = self.tail
                # self.tail.prev = self.tail.prev.prev
                self.tail.prev = self.tail.prev.prev
                self.tail.prev.next = self.tail

    def get(self, key: int) -> int:
        if key in self.hkeys.keys():
            # 删除命中的节点，再加入首部
            current_node = self.delete_node_by_key(key)
            self.insert_to_head(current_node)
            return current_node.val
        return -1

    # 从链表中抽掉，前后2个节点直接相连
    def delete_node_by_key(self, key):
        current_node = self.hkeys[key]
        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev
        return current_node

    # 最近使用过的节点，置于链表头部head哨兵之后
    def insert_to_head(self, current_node):
        first_node = self.head.next
        current_node.next = first_node
        current_node.prev = self.head
        first_node.prev = current_node
        self.head.next = current_node

    def __repr__(self):
        vals = []
        node = self.head.next
        while node.next:
            vals.append(str(node.val))
            node = node.next
        return '->'.join(vals)


if __name__ == '__main__':
    cache = LRUCache(3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.put(1, 1)
    cache.put(4, 4)
    print(cache)
    cache.get(1)  # 返回  1
    cache.put(3, 3)  # 该操作会使得密钥 2 作废
    print(cache)
    cache.get(2)  # 返回 -1 (未找到)
    cache.put(4, 4)  # 该操作会使得密钥 1 作废
    print(cache)
    cache.get(1)  # 返回 -1 (未找到)
    cache.get(3)  # 返回  3
    print(cache)
    cache.get(4)  # 返回  4
    print(cache)
