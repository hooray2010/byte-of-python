from itertools import chain
from typing import Optional

"""
当队列满时，图中的 tail 指向的位置实际上是没有存储数据的。
所以，循环队列会浪费一个数组的存储空间
"""


class CircularQueue:
    def __init__(self, capacity):
        self._capacity = capacity + 1
        self._items = [0] * self._capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, item: str) -> bool:
        if (self._tail + 1) % self._capacity == self._head:
            print("环已满，此时 tail=%s" % self._tail, end="\n")
            return False
        self._items[self._tail] = item
        self._tail = (self._tail + 1) % self._capacity
        print("新增元素 item=%s，此时 tail=%s" % (item, self._tail), end="\n")
        return True

    def dequeue(self) -> Optional[str]:
        if self._head == self._tail:
            return None
        else:
            item = self._items[self._head]
            self._head = (self._head + 1) % self._capacity
            print("出列元素 item=%s，此时 head=%s" % (item, self._head), end="\n")
            return item

    def __repr__(self) -> str:
        if self._tail >= self._head:
            return " ".join(item for item in self._items[self._head: self._tail])
        else:
            return " ".join(item for item in chain(self._items[self._head:], self._items[:self._tail]))


if __name__ == "__main__":
    q = CircularQueue(10)
    for i in range(15):
        q.enqueue(str(i))
    print(q)

    for _ in range(3):
        q.dequeue()
    print(q)

    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    q.enqueue("D")
    q.enqueue("E")
    q.enqueue("F")
    print(q)
